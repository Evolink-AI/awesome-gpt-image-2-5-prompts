# GPT Image 2.6 — 最新提示词案例

[← 全部 260 条提示词](../../README_zh-CN.md)

十条完整公开提示词：两个官方编辑示例，以及八个涵盖动画、编辑、海报与版本对比的创作者提示词。原有 250 个 GPT Image 2.5 案例保留原编号。

## 目录

  - [案例 251: 白宫环绕动画](#gpt-image-2-6-case-251)
  - [案例 252: 保留场景的花朵移除](#gpt-image-2-6-case-252)
  - [案例 253: 雪夜广告牌编辑](#gpt-image-2-6-case-253)
  - [案例 254: 持茶人像版本对比](#gpt-image-2-6-case-254)
  - [案例 255: 巴洛克冬日画框海报](#gpt-image-2-6-case-255)
  - [案例 256: 清爽角色拉伸动画](#gpt-image-2-6-case-256)
  - [案例 257: 角色吃饭表情动图](#gpt-image-2-6-case-257)
  - [案例 258: 圈选角色圣诞编辑](#gpt-image-2-6-case-258)
  - [案例 259: 角色眨眼轻晃动画](#gpt-image-2-6-case-259)
  - [案例 260: 循环动漫万花筒动画](#gpt-image-2-6-case-260)

<a id="gpt-image-2-6-case-251"></a>
### 案例 251: [白宫环绕动画](https://x.com/nima2qisi2/status/2118295936606798006) (作者 [@nima2qisi2](https://x.com/nima2qisi2))

**输入:** 公开提示词未要求提供参考图。

创作者要求生成 GIF。X 以 MP4 提供这段动画，点击预览图可播放原始动画。只有白宫片段与公开提示词相符；同一帖子中的自由女神像及故宫片段未收录。这段合成环绕动画不是实拍纪录，也不代表建筑几何已获验证。

| 输出 |
| --- |
| 原始来源媒体；参考图与生成结果的角色见各项标注。 |

[![白宫合成环绕动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

[播放创作者的环绕动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

**提示词:**

```
帮我做一个真实白宫外观的360°环绕模仿无人机拍摄，要真实还原建筑环境的实际外观情况，做成gif
```

---

<a id="gpt-image-2-6-case-252"></a>
### 案例 252: [保留场景的花朵移除](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object) (作者 [@OpenAI](https://developers.openai.com))

**输入:** 使用下方展示的参考图。

官方编辑示例。请使用所附参考照片。两个公开结果放在一起展示；这是作例，并非重复测量的基准测试。

| 输出 |
| --- |
| 原始来源媒体；参考图与生成结果的角色见各项标注。 |

<table>
<tr><td colspan="2"><strong>参考图</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-blue-hat.webp" width="360" alt="参考照片：手持花朵的男子"></td></tr>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-flare.webp" width="360" alt="保留场景的花朵移除 — GPT Image 2.6 Flare"></td><td width="50%" valign="top"><strong>GPT Image 2.6 Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-sunburst.webp" width="360" alt="保留场景的花朵移除 — GPT Image 2.6 Sunburst"></td></tr>
</table>

**提示词:**

```
Remove the flower from man's hand. Do not change anything else.
```

---

<a id="gpt-image-2-6-case-253"></a>
### 案例 253: [雪夜广告牌编辑](https://developers.openai.com/api/docs/guides/image-prompting#change-one-condition) (作者 [@OpenAI](https://developers.openai.com))

**输入:** 使用下方展示的参考图。

这是后续编辑步骤的完整提示词，并非最初生成广告牌的提示词。每个模型分别使用对应的日落广告牌图作为输入。各模型的输入与输出并排展示。

| 输出 |
| --- |
| 原始来源媒体；参考图与生成结果的角色见各项标注。 |

<table>
<tr><td width="50%" valign="top"><strong>Flare 输入</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-flare.webp" width="360" alt="雪夜广告牌编辑 — Flare 输入"></td><td width="50%" valign="top"><strong>Flare 冬季输出</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-flare.webp" width="360" alt="雪夜广告牌编辑 — Flare 冬季输出"></td></tr>
<tr><td width="50%" valign="top"><strong>Sunburst 输入</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-sunburst.webp" width="360" alt="雪夜广告牌编辑 — Sunburst 输入"></td><td width="50%" valign="top"><strong>Sunburst 冬季输出</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-sunburst.webp" width="360" alt="雪夜广告牌编辑 — Sunburst 冬季输出"></td></tr>
</table>

**提示词:**

```
Make it look like a winter evening with snowfall.
```

---

<a id="gpt-image-2-6-case-254"></a>
### 案例 254: [持茶人像版本对比](https://x.com/v3rt0x_/status/2118147596891901957) (作者 [@v3rt0x_](https://x.com/v3rt0x_))

**输入:** 公开提示词未要求提供参考图。

创作者将第一张图标为 GPT Image 2.6，第二张图标为 GPT Image 2.5。未披露具体变体、设置或重试次数。这是创作者对比，并非受控基准测试。

| 输出 |
| --- |
| 原始来源媒体；参考图与生成结果的角色见各项标注。 |

<table>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 — 创作者标注</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147098709274624.jpg" width="360" alt="持茶人像版本对比 — GPT Image 2.6 — 创作者标注"></td><td width="50%" valign="top"><strong>GPT Image 2.5 — 创作者标注</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147411746955264.jpg" width="360" alt="持茶人像版本对比 — GPT Image 2.5 — 创作者标注"></td></tr>
</table>

**提示词:**

```
a realistic photo of a woman holding a cup of tea inside her home
```

---

<a id="gpt-image-2-6-case-255"></a>
### 案例 255: [巴洛克冬日画框海报](https://x.com/Goodmanprotocol/status/2118193088128745875) (作者 [@Goodmanprotocol](https://x.com/Goodmanprotocol))

**输入:** 上传一张你有权使用的场景图。来源未单独提供原始输入图。

创作者将这些作品标注为 GPT Image 2.6 输出。两张海报都是生成结果，各自带有小幅参考图缩略图，但未单独提供原始输入图。请上传你有权使用的场景图。具体模型版本、设置和重试次数未公开。

| 输出 | 输出 2 |
| --- | --- |
| <strong>雪人画框海报</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193058370158592.jpg" width="320" alt="雪人画框海报"> | <strong>冬日村庄画框海报</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193073935245312.jpg" width="320" alt="冬日村庄画框海报"> |

**提示词:**

```
PREMIUM BAROQUE FRAMED ARTWORK - PHOTOREALISTIC GALLERY POSTER

Use the uploaded image as the sole visual reference. Create a seamless 3:4 vertical fine-art poster.

TOP SECTION (75%): Display the original scene as a beautiful painting inside an ornate antique gold Baroque frame, mounted on a subtly textured plaster wall. Preserve the original scene and its defining details. Select 1–3 prominent elements already present in the image and extend them beyond the frame in realistic 3D, with natural depth, perspective and cast shadows. Do not introduce any new objects, flowers, plants or decorative elements that are not present in the source image. Choose a muted wall color derived from the original image's palette. Match the lighting, atmosphere and time of day of the original scene. Photorealistic rendering with a sophisticated fine-art gallery aesthetic.

BOTTOM SECTION (25%): Continue the same plaster wall and lighting seamlessly. Place a small, clean thumbnail of the original unedited image slightly left of center, without a white border and with a subtle natural shadow. Beside it, add a refined 2–3-word ALL-CAPS serif title and a single-line italic subtitle inspired by the original scene. Keep the typography minimal, elegant and clearly contrasted against the wall.

COMPOSITION & QUALITY: The entire poster must appear as one continuous image. No divider lines, white bands, gaps, separate panels or outer borders. Ensure seamless transitions, balanced spacing, realistic materials, sophisticated typography and premium editorial art direction. Preserve the original subject's identity and visual character without altering the source scene.
```

---

<a id="gpt-image-2-6-case-256"></a>
### 案例 256: [清爽角色拉伸动画](https://x.com/MiraMusic_AI/status/2118168013618987298) (作者 [@MiraMusic_AI](https://x.com/MiraMusic_AI))

**输入:** 准备一张你有权使用的角色参考图。

创作者同时公开了这段完整日文动画提示词、角色设定图和生成动画。请使用你有权使用的角色参考图。具体模型版本、设置和重试次数未公开。X 以 MP4 提供所请求的 GIF，点击动画链接查看动态效果。

| 输入 | 输出 |
| --- | --- |
| <strong>创作者角色设定图</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167991833759744.jpg" width="320" alt="创作者角色设定图"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4"><strong>角色拉伸动画预览</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.jpg" width="320" alt="角色拉伸动画预览"></a> |

[播放创作者的角色拉伸动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4)

**提示词:**

```
ストレッチをしているGIFを製作してください。
仕上げはフラットでクリーンに。
複雑な微細テクスチャ、過剰な細密描写、粒状ノイズ、ザラつき、斜めグリッド状の模様なし
```

---

<a id="gpt-image-2-6-case-257"></a>
### 案例 257: [角色吃饭表情动图](https://x.com/Gorden_Sun/status/2118166046175908016) (作者 [@Gorden_Sun](https://x.com/Gorden_Sun))

**输入:** 准备一张你有权使用的角色参考图。

创作者明确说明第一个附件为生成的 GIF，第二个为角色参考图。中文提示词要求在画面上写出“真香！”。请使用你有权使用的角色参考图。具体模型版本、设置和重试次数未公开；X 以 MP4 提供动画。

| 输入 | 输出 |
| --- | --- |
| <strong>创作者角色参考图</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118166009131757568.jpg" width="320" alt="创作者角色参考图"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4"><strong>吃饭动画预览</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.jpg" width="320" alt="吃饭动画预览"></a> |

[播放创作者的吃饭动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4)

**提示词:**

```
使用这个角色，生成一张GIF图，内容是她吃大白米饭，图片里有文字：真香！
```

---

<a id="gpt-image-2-6-case-258"></a>
### 案例 258: [圈选角色圣诞编辑](https://x.com/IHayato/status/2118151619212890291) (作者 [@IHayato](https://x.com/IHayato))

**输入:** 准备一张用红圈和蓝圈标出待编辑位置的角色图。

这是创作者引用的完整日文后续编辑提示词：在红圈内添加圣诞帽，将蓝圈内的书替换为礼物。来源合成图同时展示带标注输入和编辑结果，未单独提供无标注输入图。请使用你自己标注的角色图。创作者称该编辑由 GPT Image 2.6 完成，未说明具体模型版本。

| 输出 |
| --- |
| <strong>创作者合成图：带标注输入与圣诞编辑</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151559322419200.jpg" width="640" alt="创作者合成图：带标注输入与圣诞编辑"> |

**提示词:**

```
赤丸にサンタ帽、青丸の本はプレゼントに
```

---

<a id="gpt-image-2-6-case-259"></a>
### 案例 259: [角色眨眼轻晃动画](https://x.com/IHayato/status/2118151619212890291) (作者 [@IHayato](https://x.com/IHayato))

**输入:** 准备一张你有权使用的角色参考图。

这是创作者引用的完整日文后续动画提示词。请准备你有权使用的角色参考图；来源未单独提供这段动画的输入图。同帖还含另一项圣诞编辑及价格图，此处均不作为动画输入。创作者称该结果由 GPT Image 2.6 生成，未说明具体模型版本。X 以 MP4 提供动画。

| 输出 |
| --- |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4"><strong>角色眨眼动画预览</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.jpg" width="320" alt="角色眨眼动画预览"></a> |

[播放创作者的角色眨眼动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4)

**提示词:**

```
まばたきして、ふわっと揺れて
```

---

<a id="gpt-image-2-6-case-260"></a>
### 案例 260: [循环动漫万花筒动画](https://x.com/aimikoda/status/2118665755994546650) (作者 [@aimikoda](https://x.com/aimikoda))

**输入:** 准备一张你有权使用的角色参考图。

创作者称这段动画由 GPT Image 2.6 生成。原帖展示了动画，未附原始角色参考图。X 以 MP4 格式提供这段 GIF。

| 输出 |
| --- |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.mp4"><strong>动漫万花筒动画预览</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.jpg" width="320" alt="动漫万花筒动画预览"></a> |

[播放创作者的万花筒动画](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.mp4)

**提示词:**

```
Create a seamless looping 1:1 2D anime kaleidoscope animation using the supplied character as the exact identity reference. Preserve the face, hairstyle, anatomy, outfit and visual style.

COMPOSITION: A vibrant, symmetrical kaleidoscope featuring one large central character and four surrounding copies arranged diagonally at different radial angles. Layer overlapping character portraits, decorative Japanese fans, floral motifs and colorful geometric patterns. Fill the entire frame with dense, intricate details extending beyond the edges. No circular frames.

ANIMATION: Keep the overall composition stationary while all five character instances perform independent, expressive anime movements: head tilts, blinking, playful expressions, flowing hair and rhythmic gestures. Use smooth hand-drawn animation with crisp linework, cel shading and lively secondary motion.

LOOP: All movements return naturally to their initial poses for a perfectly seamless infinite loop.

No text, logos, subtitles or additional characters.
```

---
