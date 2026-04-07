# 废片拯救 · 提示词库

本文档提供7大类废片问题的完整提示词模板，支持多平台适配。

---

## 目录

1. [清除路人/杂物](#1-清除路人杂物)
2. [修复姿势/表情](#2-修复姿势表情)
3. [调整衣服](#3-调整衣服)
4. [修复光影](#4-修复光影)
5. [调整构图](#5-调整构图)
6. [添加人物](#6-添加人物)
7. [去模糊/锐化](#7-去模糊锐化)
8. [组合修复示例](#8-组合修复示例)

---

## 1. 清除路人/杂物

### 适用场景
- 背景有陌生人、游客
- 画面中有电线杆、垃圾桶、路标等杂物
- 背景杂乱，干扰主体

### Photoshop 生成式填充

**英文版**：
```
Remove all strangers, bystanders, and unwanted objects from the background. 
Use generative fill to reconstruct clean background (wall, floor, sky, trees) with natural textures.
Keep the main subject completely untouched. No artifacts, no distortion.
```

**中文版**：
```
删除背景中所有陌生人和杂物，用生成式填充恢复干净背景（墙面/地面/天空/树木），纹理自然。
保持主体完全不变，不要产生伪影或变形。
```

### Midjourney

```
[主体描述], professional photography, clean background, no people in background
--no strangers, bystanders, crowd, unwanted objects, clutter --iw 2.5 --style raw
```

### 即梦AI/豆包

```
【主体保留】严格保持人物外貌、姿势、服装、位置完全不变
【背景清理】删除背景中所有陌生人和杂物，恢复干净背景
【风格】专业摄影，自然纹理
参考图强度：0.9
```

### NanoBanana

```
(Keep subject unchanged:2.0), (Clean background:1.5), (No strangers:1.8), (No clutter:1.5)
--no bystanders, crowd, unwanted objects --quality 2 --strength 0.3
```

### 参数建议
- **Photoshop**：选择"生成式填充"，提示词长度不超过100词
- **Midjourney**：`--iw` 设为2.0以上，确保主体一致性
- **即梦AI**：参考图强度0.85-0.9，避免主体变形

---

## 2. 修复姿势/表情

### 适用场景
- 闭眼、眨眼、表情崩坏
- 姿势僵硬、驼背
- 双下巴、表情不自然

### 通用提示词

**英文版**：
```
Fix facial expression: open closed eyes, change to natural slight smile, remove double chin.
Adjust pose: straighten spine, relax shoulders, arms hanging naturally, weight on left leg.
Keep original identity, clothing, and background completely unchanged.
NO face change, NO body shape change, ONLY expression and pose adjustment.
```

**中文版**：
```
修复表情：睁眼（修复闭眼），改为自然微笑，去除双下巴。
调整姿势：站直脊柱，放松肩膀，手臂自然下垂，重心置于左腿。
保持原有身份、服装、背景完全不变。
禁止改变面部特征，禁止改变身材，仅调整表情和姿势。
```

### 具体问题细分

#### 2.1 闭眼修复

```
Open the closed eyes. Keep eye shape and size natural. 
Maintain original eye color and gaze direction.
Add natural catchlight for lively appearance.
```

#### 2.2 表情调整

```
Change expression to [desired expression: smile/serious/surprised].
Relax facial muscles. Keep facial features unchanged.
Natural and genuine expression, no forced smile.
```

#### 2.3 姿势矫正

```
Straighten spine, correct posture.
Shoulders back and relaxed.
[Specific adjustment: turn body 15 degrees left/right]
Keep original position and background unchanged.
```

#### 2.4 去双下巴

```
Remove double chin naturally. Define jawline.
Keep facial structure unchanged. No face slimming.
Maintain natural neck appearance.
```

### 平台适配

**Midjourney**：
```
[Original subject], natural smile, open eyes, good posture
--no closed eyes, double chin, bad posture --iw 2.5
```

**即梦AI**：
```
【主体特征锁定】[详细描述人物特征]
【表情调整】睁眼，自然微笑，去除双下巴
【姿势调整】站直，放松肩膀，自然站立
【禁止变异】禁止改变面部、身材、服装
参考图强度：0.88
```

---

## 3. 调整衣服

### 适用场景
- 衣服颜色不满意
- 衣服有褶皱
- 衣服风格与场景不搭

### 改衣服颜色

**英文版**：
```
Recolor the [shirt/dress/jacket] to [target color: e.g., dark blue, hex #1e3a8a].
Remove all wrinkles and folds. Smooth fabric surface.
Enhance fabric texture to [cotton/silk/wool].
Keep the same silhouette, fit, and lighting direction.
NO change to body shape, pose, or background.
```

**中文版**：
```
将[上衣/裙子/外套]改为[目标颜色]。
去除所有褶皱，平滑面料表面。
优化面料质感为[棉质/丝绸/羊毛]。
保持轮廓、版型、光影方向不变。
禁止改变身材、姿势、背景。
```

### 去除褶皱

```
Remove all wrinkles and folds from [clothing item].
Smooth fabric texture while maintaining natural drape.
Preserve clothing design and fit.
Keep original lighting and shadows on fabric.
```

### 改变风格

```
Transform [clothing item] to [style: casual/formal/vintage].
Adjust details: [specific changes].
Maintain body proportions and pose.
Match existing lighting conditions.
```

### 平台适配

**Midjourney**：
```
[Subject description], wearing [color] [clothing type], [fabric texture]
--no wrinkles, folds --iw 2.0
```

**即梦AI**：
```
【服装改造】将[衣服]改为[颜色]，去除褶皱
【主体保持】人物外貌、姿势、位置完全不变
【光影一致】保持原有光影方向
参考图强度：0.85
```

---

## 4. 修复光影

### 适用场景
- 逆光导致面部死黑
- 光线过曝/过暗
- 阴阳脸、阴影脏乱

### 逆光修复

**英文版**：
```
Brighten face to natural skin tone (increase exposure by 1-1.5 stops).
Reduce harsh backlight effect. Add soft fill light from front.
Lower highlight on forehead and cheeks. Increase shadow detail by 40-50%.
Maintain background exposure. Keep natural lighting atmosphere.
```

**中文版**：
```
提亮面部至自然肤色（曝光+1~1.5档）。
减弱逆光效果，添加正面柔光补光。
降低额头和脸颊的高光，提升阴影细节40-50%。
保持背景曝光不变，维持自然光影氛围。
```

### 过暗修复

```
Increase overall brightness by [stops]. 
Brighten shadows, reveal details in dark areas.
Add fill light to reduce harsh shadows.
Maintain contrast and avoid overexposure.
Keep natural color temperature.
```

### 过曝修复

```
Reduce highlight exposure. Recover details in bright areas.
Add subtle shadows for depth. Lower overall exposure by [stops].
Maintain skin texture and natural appearance.
No loss of detail in midtones.
```

### 阴阳脸修复

```
Balance lighting between left and right face.
Add fill light to shadow side. Reduce contrast by [percentage].
Maintain natural lighting direction. Keep three-dimensional feel.
Even out skin tone on both sides.
```

### 平台适配

**Lightroom参数**：
```
曝光: +1.0
阴影: +40
高光: -30
对比度: +10
清晰度: +15
```

**即梦AI**：
```
【光影调整】提亮面部，添加正面柔光
【参数】曝光+1档，阴影细节+40%
【主体保持】人物特征完全不变
参考图强度：0.9
```

### 与ai-relighting配合
对于复杂的光影问题（如电影风格光影重构），建议引用 `ai-relighting` Skill的专业能力。

---

## 5. 调整构图

### 适用场景
- 照片歪斜
- 构图失衡
- 主体位置不佳

### 裁剪构图

**英文版**：
```
Straighten horizon. Crop to [aspect ratio: 4:5, 1:1, 16:9].
Place main subject on [left/right] third according to rule of thirds.
Remove [10-20%] from top/bottom as needed.
Maintain subject proportions and image quality.
```

**中文版**：
```
拉平地平线，裁剪为[比例]。
按三分法将主体置于[左/右]三分之一处。
必要时上下各裁切[百分比]。
保持主体比例和画质不变。
```

### 旋转调整

```
Rotate image [degrees] clockwise/counter-clockwise.
Straighten [horizon/building lines].
Maintain subject position relative to frame.
```

### 平台适配

**Lightroom**：
```
裁剪工具: 设置比例 4:5
旋转角度: [度数]
构图参考线: 三分法
```

**Midjourney**：
```
[Subject], [composition], [aspect ratio]
--ar 4:5 --style raw
```

---

## 6. 添加人物

### 适用场景
- 合影缺人
- 需要添加某人到画面中

### 基础提示词

**英文版**：
```
Add a [gender: male/female] person of [approximate height] on the [left/right] side.
[Appearance: hair color, age, build].
[Clothing: color, type, style].
Standing next to main subject, facing camera, [expression: natural smile].
Match existing lighting: direction, color temperature, shadow softness.
Consistent depth of field. Natural integration with scene.
```

**中文版**：
```
在[左/右]侧添加一名[性别]、[大概身高]的人物。
[外貌：发色、年龄、体型]。
[服装：颜色、款式、风格]。
站在主体旁边，面朝镜头，[表情：自然微笑]。
光影匹配：方向、色温、阴影柔硬度与主图一致。
景深保持一致，自然融入场景。
```

### 详细示例

```
Add a female person (approx. 165cm tall) on the left side.
Long brown hair, mid-20s, slim build.
Wearing white summer dress, casual style.
Standing naturally next to the main subject, gentle smile.
Front lighting matching the scene, soft shadows.
Background blur consistent with original.
```

### 平台适配

**Photoshop生成式填充**：
```
选区工具框选添加位置 → 生成式填充 → 描述人物特征
提示词: "A [description] person standing naturally, matching lighting"
```

**Midjourney**：
```
[Original scene with added person description]
--iw 1.5 --style raw
```

---

## 7. 去模糊/锐化

### 适用场景
- 手抖导致模糊
- 跑焦、对焦失败
- 运动模糊

### 基础提示词

**英文版**：
```
Apply AI deblur to entire image. 
Sharpen eyes, eyebrows, and lips (strength 60-70%).
Remove motion blur trail. 
Add subtle texture to skin and hair.
Keep background slightly soft (Gaussian blur radius 1-2px) to enhance subject focus.
Maintain natural appearance, no over-sharpening artifacts.
```

**中文版**：
```
全局AI去模糊。
锐化眼睛、眉毛、嘴唇（强度60-70%）。
移除运动模糊痕迹。
为皮肤和头发增加细微纹理。
保持背景轻微柔化（高斯模糊1-2px）以突出主体。
保持自然外观，避免过度锐化产生伪影。
```

### 平台适配

**Photoshop**：
```
滤镜 → 智能锐化
数量: 100-150%
半径: 1-2像素
减少杂色: 10-20%
```

**Lightroom**：
```
清晰度: +30
锐化 → 数量: 60
锐化 → 半径: 1.0
锐化 → 细节: 50
```

**Topaz Sharpen AI**：
```
模式: Motion Blur / Out of Focus
强度: 中等
```

---

## 8. 组合修复示例

### 8.1 路人 + 逆光 + 表情

**输入**：`/clean + /light 逆光 + /face`

**输出**（按注意力权重排序）：

```
【步骤1 - 修复逆光】（权重最高）
提亮面部至自然肤色，曝光+1.2档。
减弱逆光，添加正面柔光补光。
降低额头高光，提升阴影细节45%。
保持背景曝光不变。

【步骤2 - 清除路人】
删除背景所有陌生人，用生成式填充恢复干净背景。
保持主体完全不变，无伪影。

【步骤3 - 修复表情】
睁眼，改为自然微笑，去除双下巴。
保持面部特征、身材、服装不变。
```

### 8.2 衣服改色 + 姿势调整 + 锐化

**输入**：`/cloth 深蓝色 + /pose + /sharpen`

**输出**：

```
【步骤1 - 衣服改色】
将上衣改为深蓝色（#1e3a8a）。
去除褶皱，优化棉质面料质感。
保持轮廓和光影方向不变。

【步骤2 - 调整姿势】
站直脊柱，放松肩膀，身体右转15度。
手臂自然下垂，重心置于左腿。
保持面部表情、服装颜色不变。

【步骤3 - 锐化去模糊】
AI去模糊，锐化眼睛和嘴唇（强度70%）。
保持背景轻微柔化，突出主体。
```

### 8.3 一键全修复

**输入**：`/megafix`

**输出**：

```
【完整修复方案】

步骤1 | 光影修复
- 提亮面部至自然肤色（曝光+1.5档）
- 添加正面柔光，降低高光
- 提升阴影细节50%
- 保持自然光影氛围

步骤2 | 清除干扰
- 删除所有路人、杂物
- 用生成式填充恢复干净背景
- 保持主体完全不变

步骤3 | 修复主体
- 睁眼，自然微笑，去双下巴
- 站直脊柱，放松肩膀
- 保持身份特征不变

步骤4 | 优化细节
- 去除衣服褶皱
- 优化面料质感
- 保持轮廓不变

步骤5 | 锐化输出
- AI去模糊，锐化关键部位
- 保持背景柔化
- 最终质量检查
```

---

## 使用建议

### 提示词优化技巧

1. **具体化**：避免"好看一点"，使用"曝光+1档""锐化强度70%"
2. **保留指令**：始终强调"保持主体不变""禁止改变面部特征"
3. **负面约束**：明确列出"NO face change, NO body change"
4. **权重控制**：重要内容放在前面，使用大写强调

### 平台选择建议

- **Photoshop**：适合精确控制，局部修复
- **Midjourney**：适合创意重构，风格化处理
- **即梦AI/豆包**：中文友好，适合快速修复
- **Lightroom**：适合光影调整，批量处理
- **Topaz**：专业去模糊、降噪

### 避免常见错误

- ❌ 一次性修复所有问题 → 分步处理
- ❌ 只说"要改什么" → 加上"不要改什么"
- ❌ 过度依赖AI → 保存中间版本，逐步优化

---

**提示词库持续更新中，根据用户反馈不断优化。**
