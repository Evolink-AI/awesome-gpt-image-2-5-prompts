# GPT Image 2.6 — 最新のプロンプト作例

[← 全254件のプロンプト](../../README_ja.md)

全文公開のプロンプト4件です。公式の編集例2件、作者によるアニメーション1件、作者によるバージョン比較1件を収録しています。既存のGPT Image 2.5の250ケースは番号を維持しています。

## 目次

  - [ケース 251: ホワイトハウスの周回アニメーション](#gpt-image-2-6-case-251)
  - [ケース 252: 周囲を保ったまま花を除去](#gpt-image-2-6-case-252)
  - [ケース 253: 雪の夕景に変える看板編集](#gpt-image-2-6-case-253)
  - [ケース 254: 紅茶を持つ人物写真のバージョン比較](#gpt-image-2-6-case-254)

<a id="gpt-image-2-6-case-251"></a>
### ケース 251: [ホワイトハウスの周回アニメーション](https://x.com/nima2qisi2/status/2118295936606798006) (投稿者 [@nima2qisi2](https://x.com/nima2qisi2))

**入力:** 公開されたプロンプトでは参照画像は指定されていません。

作者はGIFを指定しています。XではこのアニメーションをMP4として配信しており、プレビュー画像から元のアニメーションを再生できます。公開プロンプトに対応するのはホワイトハウスの動画のみで、同じ投稿の自由の女神像と紫禁城の動画は除外しています。この合成された周回映像は、記録映像や検証済みの建築形状を示すものではありません。

| 出力 |
| --- |
| 出典の画像・動画。参照画像と生成結果の役割は各表示に記載しています。 |

[![ホワイトハウスの合成周回アニメーション](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

[作者の周回アニメーションを再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

**プロンプト:**

```
帮我做一个真实白宫外观的360°环绕模仿无人机拍摄，要真实还原建筑环境的实际外观情况，做成gif
```

---

<a id="gpt-image-2-6-case-252"></a>
### ケース 252: [周囲を保ったまま花を除去](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object) (投稿者 [@OpenAI](https://developers.openai.com))

**入力:** 以下に示す参照画像を使ってください。

公式の編集例です。掲載された参照写真を使用してください。公開された両モデルの結果を並べて表示しています。反復測定したベンチマークではありません。

| 出力 |
| --- |
| 出典の画像・動画。参照画像と生成結果の役割は各表示に記載しています。 |

<table>
<tr><td colspan="2"><strong>参照画像</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-blue-hat.webp" width="360" alt="参照写真：花を手に持つ男性"></td></tr>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-flare.webp" width="360" alt="周囲を保ったまま花を除去 — GPT Image 2.6 Flare"></td><td width="50%" valign="top"><strong>GPT Image 2.6 Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-sunburst.webp" width="360" alt="周囲を保ったまま花を除去 — GPT Image 2.6 Sunburst"></td></tr>
</table>

**プロンプト:**

```
Remove the flower from man's hand. Do not change anything else.
```

---

<a id="gpt-image-2-6-case-253"></a>
### ケース 253: [雪の夕景に変える看板編集](https://developers.openai.com/api/docs/guides/image-prompting#change-one-condition) (投稿者 [@OpenAI](https://developers.openai.com))

**入力:** 以下に示す参照画像を使ってください。

これは後続の編集に使うプロンプト全文で、看板を最初に生成したプロンプトではありません。各モデルには、それぞれに対応する夕景の看板画像を入力してください。モデルごとの入力と出力を横に並べて表示しています。

| 出力 |
| --- |
| 出典の画像・動画。参照画像と生成結果の役割は各表示に記載しています。 |

<table>
<tr><td width="50%" valign="top"><strong>Flareの入力</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-flare.webp" width="360" alt="雪の夕景に変える看板編集 — Flareの入力"></td><td width="50%" valign="top"><strong>Flareの雪景色の出力</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-flare.webp" width="360" alt="雪の夕景に変える看板編集 — Flareの雪景色の出力"></td></tr>
<tr><td width="50%" valign="top"><strong>Sunburstの入力</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-sunburst.webp" width="360" alt="雪の夕景に変える看板編集 — Sunburstの入力"></td><td width="50%" valign="top"><strong>Sunburstの雪景色の出力</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-sunburst.webp" width="360" alt="雪の夕景に変える看板編集 — Sunburstの雪景色の出力"></td></tr>
</table>

**プロンプト:**

```
Make it look like a winter evening with snowfall.
```

---

<a id="gpt-image-2-6-case-254"></a>
### ケース 254: [紅茶を持つ人物写真のバージョン比較](https://x.com/v3rt0x_/status/2118147596891901957) (投稿者 [@v3rt0x_](https://x.com/v3rt0x_))

**入力:** 公開されたプロンプトでは参照画像は指定されていません。

作者は1枚目をGPT Image 2.6、2枚目をGPT Image 2.5と記載しています。モデルの派生版、設定、試行回数は公開されていません。作者による比較であり、条件を統制したベンチマークではありません。

| 出力 |
| --- |
| 出典の画像・動画。参照画像と生成結果の役割は各表示に記載しています。 |

<table>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 — 作者の表記</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147098709274624.jpg" width="360" alt="紅茶を持つ人物写真のバージョン比較 — GPT Image 2.6 — 作者の表記"></td><td width="50%" valign="top"><strong>GPT Image 2.5 — 作者の表記</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147411746955264.jpg" width="360" alt="紅茶を持つ人物写真のバージョン比較 — GPT Image 2.5 — 作者の表記"></td></tr>
</table>

**プロンプト:**

```
a realistic photo of a woman holding a cup of tea inside her home
```

---
