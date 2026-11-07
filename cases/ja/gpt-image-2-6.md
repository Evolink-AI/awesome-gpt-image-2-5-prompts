# GPT Image 2.6 — 最新のプロンプト作例

[← 全260件のプロンプト](../../README_ja.md)

全文公開のプロンプト10件です。公式の編集例2件と、アニメーション、編集、ポスター、バージョン比較を扱う作者によるプロンプト8件を収録しています。既存のGPT Image 2.5の250ケースは番号を維持しています。

## 目次

  - [ケース 251: ホワイトハウスの周回アニメーション](#gpt-image-2-6-case-251)
  - [ケース 252: 周囲を保ったまま花を除去](#gpt-image-2-6-case-252)
  - [ケース 253: 雪の夕景に変える看板編集](#gpt-image-2-6-case-253)
  - [ケース 254: 紅茶を持つ人物写真のバージョン比較](#gpt-image-2-6-case-254)
  - [ケース 255: バロック額縁の冬のギャラリーポスター](#gpt-image-2-6-case-255)
  - [ケース 256: クリーンなキャラクターストレッチ動画](#gpt-image-2-6-case-256)
  - [ケース 257: ご飯を食べるキャラクタースタンプ](#gpt-image-2-6-case-257)
  - [ケース 258: 丸印で指定するキャラクターのクリスマス編集](#gpt-image-2-6-case-258)
  - [ケース 259: まばたきと揺れのキャラクターアニメーション](#gpt-image-2-6-case-259)
  - [ケース 260: アニメ風の万華鏡ループ動画](#gpt-image-2-6-case-260)

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

<a id="gpt-image-2-6-case-255"></a>
### ケース 255: [バロック額縁の冬のギャラリーポスター](https://x.com/Goodmanprotocol/status/2118193088128745875) (投稿者 [@Goodmanprotocol](https://x.com/Goodmanprotocol))

**入力:** 使用権限のある風景画像を1枚アップロードします。出典には独立した元の入力画像はありません。

作者がGPT Image 2.6の出力として公開した作例です。2枚とも生成結果のポスターで、それぞれに小さな参照画像のサムネイルがありますが、独立した元の入力画像は公開されていません。使用権限のある自分の風景画像をアップロードしてください。モデルの種類、設定、再試行回数は明らかにされていません。

| 出力 | 出力 2 |
| --- | --- |
| <strong>雪だるまギャラリーポスター</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193058370158592.jpg" width="320" alt="雪だるまギャラリーポスター"> | <strong>冬の村のギャラリーポスター</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193073935245312.jpg" width="320" alt="冬の村のギャラリーポスター"> |

**プロンプト:**

```
PREMIUM BAROQUE FRAMED ARTWORK - PHOTOREALISTIC GALLERY POSTER

Use the uploaded image as the sole visual reference. Create a seamless 3:4 vertical fine-art poster.

TOP SECTION (75%): Display the original scene as a beautiful painting inside an ornate antique gold Baroque frame, mounted on a subtly textured plaster wall. Preserve the original scene and its defining details. Select 1–3 prominent elements already present in the image and extend them beyond the frame in realistic 3D, with natural depth, perspective and cast shadows. Do not introduce any new objects, flowers, plants or decorative elements that are not present in the source image. Choose a muted wall color derived from the original image's palette. Match the lighting, atmosphere and time of day of the original scene. Photorealistic rendering with a sophisticated fine-art gallery aesthetic.

BOTTOM SECTION (25%): Continue the same plaster wall and lighting seamlessly. Place a small, clean thumbnail of the original unedited image slightly left of center, without a white border and with a subtle natural shadow. Beside it, add a refined 2–3-word ALL-CAPS serif title and a single-line italic subtitle inspired by the original scene. Keep the typography minimal, elegant and clearly contrasted against the wall.

COMPOSITION & QUALITY: The entire poster must appear as one continuous image. No divider lines, white bands, gaps, separate panels or outer borders. Ensure seamless transitions, balanced spacing, realistic materials, sophisticated typography and premium editorial art direction. Preserve the original subject's identity and visual character without altering the source scene.
```

---

<a id="gpt-image-2-6-case-256"></a>
### ケース 256: [クリーンなキャラクターストレッチ動画](https://x.com/MiraMusic_AI/status/2118168013618987298) (投稿者 [@MiraMusic_AI](https://x.com/MiraMusic_AI))

**入力:** 使用権限のあるキャラクター参照画像を用意します。

作者はキャラクター設定画と生成アニメーションを、この日本語プロンプトの全文とともに公開しています。使用権限のあるキャラクター参照画像を使ってください。モデルの種類、設定、再試行回数は明らかにされていません。Xでは指定されたGIFをMP4として配信しており、動きはリンク先のアニメーションで確認できます。

| 入力 | 出力 |
| --- | --- |
| <strong>作者のキャラクター設定画</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167991833759744.jpg" width="320" alt="作者のキャラクター設定画"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4"><strong>ストレッチ動画のプレビュー</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.jpg" width="320" alt="ストレッチ動画のプレビュー"></a> |

[作者のストレッチアニメーションを再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4)

**プロンプト:**

```
ストレッチをしているGIFを製作してください。
仕上げはフラットでクリーンに。
複雑な微細テクスチャ、過剰な細密描写、粒状ノイズ、ザラつき、斜めグリッド状の模様なし
```

---

<a id="gpt-image-2-6-case-257"></a>
### ケース 257: [ご飯を食べるキャラクタースタンプ](https://x.com/Gorden_Sun/status/2118166046175908016) (投稿者 [@Gorden_Sun](https://x.com/Gorden_Sun))

**入力:** 使用権限のあるキャラクター参照画像を用意します。

作者は1つ目の添付を生成GIF、2つ目をキャラクターの参照画像と明記しています。中国語のプロンプトは、画像内に「真香！」という文字を入れるよう指定しています。使用権限のあるキャラクター参照画像を使ってください。モデルの種類、設定、再試行回数は明らかにされていません。XではアニメーションをMP4として配信しています。

| 入力 | 出力 |
| --- | --- |
| <strong>作者のキャラクター参照画像</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118166009131757568.jpg" width="320" alt="作者のキャラクター参照画像"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4"><strong>ご飯動画のプレビュー</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.jpg" width="320" alt="ご飯動画のプレビュー"></a> |

[作者のご飯アニメーションを再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4)

**プロンプト:**

```
使用这个角色，生成一张GIF图，内容是她吃大白米饭，图片里有文字：真香！
```

---

<a id="gpt-image-2-6-case-258"></a>
### ケース 258: [丸印で指定するキャラクターのクリスマス編集](https://x.com/IHayato/status/2118151619212890291) (投稿者 [@IHayato](https://x.com/IHayato))

**入力:** 編集箇所を赤丸と青丸で示したキャラクター画像を用意します。

作者が引用した日本語の追加編集プロンプトの全文です。赤丸にサンタ帽を加え、青丸内の本をプレゼントに置き換える指示です。出典の比較画像には、印を付けた入力と編集結果が一緒に示されていますが、印のない入力画像は別途公開されていません。自分で印を付けたキャラクター画像を用意してください。作者はGPT Image 2.6による編集と説明していますが、モデルの種類は明記していません。

| 出力 |
| --- |
| <strong>作者の比較画像：印を付けた入力とクリスマス編集</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151559322419200.jpg" width="640" alt="作者の比較画像：印を付けた入力とクリスマス編集"> |

**プロンプト:**

```
赤丸にサンタ帽、青丸の本はプレゼントに
```

---

<a id="gpt-image-2-6-case-259"></a>
### ケース 259: [まばたきと揺れのキャラクターアニメーション](https://x.com/IHayato/status/2118151619212890291) (投稿者 [@IHayato](https://x.com/IHayato))

**入力:** 使用権限のあるキャラクター参照画像を用意します。

作者が引用した日本語の追加アニメーションプロンプトの全文です。使用権限のあるキャラクター参照画像を用意してください。このアニメーション用の独立した入力画像は公開されていません。同じ投稿には別のクリスマス編集と料金の図もありますが、ここではどちらもアニメーションの入力として扱っていません。作者はGPT Image 2.6による結果と説明していますが、モデルの種類は明記していません。XではアニメーションをMP4として配信しています。

| 出力 |
| --- |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4"><strong>まばたき動画のプレビュー</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.jpg" width="320" alt="まばたき動画のプレビュー"></a> |

[作者のまばたきアニメーションを再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4)

**プロンプト:**

```
まばたきして、ふわっと揺れて
```

---

<a id="gpt-image-2-6-case-260"></a>
### ケース 260: [アニメ風の万華鏡ループ動画](https://x.com/aimikoda/status/2118665755994546650) (投稿者 [@aimikoda](https://x.com/aimikoda))

**入力:** 使用権限のあるキャラクター参照画像を用意します。

作者は、このアニメーションをGPT Image 2.6で制作したと説明しています。投稿にはアニメーションが掲載されており、元のキャラクター参照画像は公開されていません。XではGIFをMP4として配信しています。

| 出力 |
| --- |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.mp4"><strong>アニメ風万華鏡動画のプレビュー</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.jpg" width="320" alt="アニメ風万華鏡動画のプレビュー"></a> |

[作者の万華鏡アニメーションを再生](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.mp4)

**プロンプト:**

```
Create a seamless looping 1:1 2D anime kaleidoscope animation using the supplied character as the exact identity reference. Preserve the face, hairstyle, anatomy, outfit and visual style.

COMPOSITION: A vibrant, symmetrical kaleidoscope featuring one large central character and four surrounding copies arranged diagonally at different radial angles. Layer overlapping character portraits, decorative Japanese fans, floral motifs and colorful geometric patterns. Fill the entire frame with dense, intricate details extending beyond the edges. No circular frames.

ANIMATION: Keep the overall composition stationary while all five character instances perform independent, expressive anime movements: head tilts, blinking, playful expressions, flowing hair and rhythmic gestures. Use smooth hand-drawn animation with crisp linework, cel shading and lively secondary motion.

LOOP: All movements return naturally to their initial poses for a perfectly seamless infinite loop.

No text, logos, subtitles or additional characters.
```

---
