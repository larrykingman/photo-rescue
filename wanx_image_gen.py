#!/usr/bin/env python3
"""
废片拯救 - wan2.7图像生成工具（开发者模式）

使用阿里云百炼wan2.7模型进行图像生成和编辑
支持：文生图、图生图、图像编辑
自动压缩过大图片，用户无需配置API Key

使用方式：
    # 文生图
    python scripts/wanx_image_gen.py --prompt "描述文字" --output output.png
    
    # 图生图（废片拯救）
    python scripts/wanx_image_gen.py --input original.jpg --prompt "修复描述" --output fixed.png
"""

import argparse
import base64
import io
import json
import os
import random
import sys
import time
from pathlib import Path
from PIL import Image

from coze_workload_identity import requests


# 内置API Key列表（开发者模式）
API_KEYS = [
    "sk-5ff36ee4460b4385a426e34db4d70b0d",
    "sk-02791f4e5ceb44ca99322e78c03e5ec1"
]

# 图片大小限制（5MB）
MAX_IMAGE_SIZE = 5 * 1024 * 1024
# 最大图片尺寸
MAX_DIMENSION = 2048


def get_api_key():
    """
    获取API凭证（开发者模式）
    
    随机选择一个可用的API Key
    """
    return random.choice(API_KEYS)


def compress_image(input_path: str, output_path: str = None, max_size: int = MAX_IMAGE_SIZE, max_dimension: int = MAX_DIMENSION):
    """
    压缩图片，确保图片大小和尺寸在限制范围内
    
    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径（如果为None，则覆盖原图）
        max_size: 最大文件大小（字节）
        max_dimension: 最大边长（像素）
    
    Returns:
        压缩后的图片路径
    """
    if output_path is None:
        output_path = input_path
    
    # 读取图片
    img = Image.open(input_path)
    
    # 记录原始格式
    original_format = img.format
    
    # 如果图片过大，先缩放尺寸
    width, height = img.size
    if width > max_dimension or height > max_dimension:
        # 计算缩放比例
        ratio = min(max_dimension / width, max_dimension / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # 逐步降低质量直到文件大小符合要求
    quality = 95
    while quality >= 50:
        buffer = io.BytesIO()
        # 保持原始格式
        save_format = original_format if original_format in ['JPEG', 'PNG', 'WEBP'] else 'JPEG'
        img.save(buffer, format=save_format, quality=quality, optimize=True)
        
        if buffer.tell() <= max_size:
            # 文件大小符合要求，保存
            with open(output_path, 'wb') as f:
                f.write(buffer.getvalue())
            return output_path
        
        quality -= 10
    
    # 如果质量降到最低仍不符合要求，使用最低质量保存
    buffer.seek(0)
    img.save(buffer, format='JPEG', quality=50, optimize=True)
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())
    
    return output_path


def prepare_image(input_path: str, temp_dir: str = None) -> str:
    """
    准备图片：如果是过大的图片则自动压缩
    
    Args:
        input_path: 输入图片路径
        temp_dir: 临时目录
    
    Returns:
        处理后的图片路径（可能是压缩后的）
    """
    # 检查文件大小
    file_size = os.path.getsize(input_path)
    
    if file_size > MAX_IMAGE_SIZE:
        # 需要压缩
        print(f"🔄 图片过大（{file_size / 1024 / 1024:.2f}MB），正在优化...")
        
        # 创建临时目录
        if temp_dir is None:
            temp_dir = os.path.dirname(input_path) or '.'
        
        temp_path = os.path.join(temp_dir, f"_temp_compressed_{int(time.time())}.jpg")
        
        # 压缩图片
        compress_image(input_path, temp_path)
        
        return temp_path
    
    # 图片大小合适，返回原路径
    return input_path


def text_to_image(prompt: str, output_path: str, size: str = "1024*1024"):
    """
    文生图 - 使用wan2.7模型生成图片
    
    Args:
        prompt: 文本描述
        output_path: 输出图片路径
        size: 图片尺寸，默认1024*1024
    """
    api_key = get_api_key()
    
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable"
    }
    
    payload = {
        "model": "wanx-v1",
        "input": {
            "prompt": prompt
        },
        "parameters": {
            "size": size,
            "n": 1,
            "style": "<auto>"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        
        if response.status_code >= 400:
            raise Exception(f"API请求失败: 状态码 {response.status_code}, 响应: {response.text}")
        
        result = response.json()
        
        task_id = result.get("output", {}).get("task_id")
        if not task_id:
            raise Exception(f"未获取到任务ID: {result}")
        
        image_url = poll_task_status(task_id, api_key)
        download_image(image_url, output_path)
        
        print(f"✅ 图片已生成: {output_path}")
        return output_path
        
    except Exception as e:
        raise Exception(f"文生图失败: {str(e)}")


def image_to_image(input_image: str, prompt: str, output_path: str, strength: float = 0.7):
    """
    图生图 - 使用wan2.7模型进行图像编辑（废片拯救核心功能）
    
    Args:
        input_image: 输入图片路径
        prompt: 修改描述
        output_path: 输出图片路径
        strength: 修改强度（0-1），值越小保持原图越多
    """
    api_key = get_api_key()
    
    # 准备图片（如果过大则压缩）
    processed_image = prepare_image(input_image)
    
    # 读取并编码输入图片
    with open(processed_image, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    # 如果是临时压缩文件，清理
    if processed_image != input_image and os.path.exists(processed_image):
        try:
            os.remove(processed_image)
        except:
            pass
    
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/image2image/image-synthesis"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable"
    }
    
    payload = {
        "model": "wanx-v1",
        "input": {
            "image": image_data,
            "prompt": prompt
        },
        "parameters": {
            "strength": strength,
            "n": 1
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        
        if response.status_code >= 400:
            raise Exception(f"API请求失败: 状态码 {response.status_code}, 响应: {response.text}")
        
        result = response.json()
        
        task_id = result.get("output", {}).get("task_id")
        if not task_id:
            raise Exception(f"未获取到任务ID: {result}")
        
        image_url = poll_task_status(task_id, api_key)
        download_image(image_url, output_path)
        
        print(f"✅ 图片已生成: {output_path}")
        return output_path
        
    except Exception as e:
        raise Exception(f"图生图失败: {str(e)}")


def poll_task_status(task_id: str, api_key: str, max_wait: int = 300):
    """
    查询异步任务状态，直到完成
    
    Args:
        task_id: 任务ID
        api_key: API密钥
        max_wait: 最大等待时间（秒）
    
    Returns:
        生成的图片URL
    """
    url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    start_time = time.time()
    
    while time.time() - start_time < max_wait:
        try:
            response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code >= 400:
                raise Exception(f"查询任务失败: {response.text}")
            
            result = response.json()
            status = result.get("output", {}).get("task_status")
            
            if status == "SUCCEEDED":
                results = result.get("output", {}).get("results", [])
                if results and len(results) > 0:
                    return results[0].get("url")
                else:
                    raise Exception("任务成功但未返回图片URL")
            
            elif status == "FAILED":
                error_msg = result.get("output", {}).get("message", "未知错误")
                raise Exception(f"任务失败: {error_msg}")
            
            elif status in ["PENDING", "RUNNING"]:
                time.sleep(3)
            
            else:
                raise Exception(f"未知任务状态: {status}")
        
        except Exception as e:
            if "查询任务失败" in str(e):
                raise
            print(f"⚠️ 查询异常: {str(e)}, 重试中...")
            time.sleep(2)
    
    raise Exception(f"任务超时（超过{max_wait}秒）")


def download_image(url: str, output_path: str):
    """
    下载图片
    
    Args:
        url: 图片URL
        output_path: 保存路径
    """
    response = requests.get(url, timeout=30)
    
    if response.status_code >= 400:
        raise Exception(f"下载图片失败: 状态码 {response.status_code}")
    
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "wb") as f:
        f.write(response.content)


def main():
    parser = argparse.ArgumentParser(
        description="废片拯救 - wan2.7图像生成工具（开发者模式）"
    )
    
    parser.add_argument(
        "--prompt", "-p",
        required=True,
        help="文本描述或修改指令"
    )
    
    parser.add_argument(
        "--input", "-i",
        help="输入图片路径（图生图模式）"
    )
    
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="输出图片路径"
    )
    
    parser.add_argument(
        "--size", "-s",
        default="1024*1024",
        help="图片尺寸（仅文生图模式），默认1024*1024"
    )
    
    parser.add_argument(
        "--strength",
        type=float,
        default=0.7,
        help="修改强度（仅图生图模式，0-1），默认0.7"
    )
    
    args = parser.parse_args()
    
    try:
        if args.input:
            if not Path(args.input).exists():
                print(f"❌ 错误: 输入图片不存在: {args.input}", file=sys.stderr)
                sys.exit(1)
            
            print(f"🔄 正在使用wan2.7模型拯救废片...")
            print(f"   输入: {args.input}")
            print(f"   指令: {args.prompt}")
            
            image_to_image(
                input_image=args.input,
                prompt=args.prompt,
                output_path=args.output,
                strength=args.strength
            )
        else:
            print(f"🎨 正在使用wan2.7模型生成图片...")
            print(f"   描述: {args.prompt}")
            
            text_to_image(
                prompt=args.prompt,
                output_path=args.output,
                size=args.size
            )
    
    except Exception as e:
        print(f"❌ 错误: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
