# GPT Image 2.6 — 最新提示词案例

[← 全部 254 条提示词](../../README_zh-CN.md)

四条完整公开提示词：两个官方编辑示例、一个创作者动画与一个创作者版本对比。原有 250 个 GPT Image 2.5 案例保留原编号。

## 目录

  - [案例 251: 白宫环绕动画](#gpt-image-2-6-case-251)
  - [案例 252: 保留场景的花朵移除](#gpt-image-2-6-case-252)
  - [案例 253: 雪夜广告牌编辑](#gpt-image-2-6-case-253)
  - [案例 254: 持茶人像版本对比](#gpt-image-2-6-case-254)

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
