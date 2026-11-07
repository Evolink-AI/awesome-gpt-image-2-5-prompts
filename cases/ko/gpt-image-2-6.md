# GPT Image 2.6 — 최신 프롬프트 사례

[← 전체 프롬프트 260개](../../README_ko.md)

전문이 공개된 프롬프트 10개입니다. 공식 편집 예시 2개와 애니메이션, 편집, 포스터, 버전 비교를 다루는 제작자 프롬프트 8개를 수록했습니다. 기존 GPT Image 2.5 사례 250개의 번호는 유지합니다.

## 목차

  - [사례 251: 백악관 주위 회전 애니메이션](#gpt-image-2-6-case-251)
  - [사례 252: 주변 장면을 유지하며 꽃 제거](#gpt-image-2-6-case-252)
  - [사례 253: 눈 내리는 저녁의 광고판 편집](#gpt-image-2-6-case-253)
  - [사례 254: 차를 든 인물 사진 버전 비교](#gpt-image-2-6-case-254)
  - [사례 255: 바로크 액자의 겨울 갤러리 포스터](#gpt-image-2-6-case-255)
  - [사례 256: 깔끔한 캐릭터 스트레칭 애니메이션](#gpt-image-2-6-case-256)
  - [사례 257: 밥 먹는 캐릭터 스티커](#gpt-image-2-6-case-257)
  - [사례 258: 원 표시로 지정하는 캐릭터 크리스마스 편집](#gpt-image-2-6-case-258)
  - [사례 259: 눈을 깜박이며 흔들리는 캐릭터 애니메이션](#gpt-image-2-6-case-259)
  - [사례 260: 애니메이션풍 만화경 루프 영상](#gpt-image-2-6-case-260)

<a id="gpt-image-2-6-case-251"></a>
### 사례 251: [백악관 주위 회전 애니메이션](https://x.com/nima2qisi2/status/2118295936606798006) (작성자 [@nima2qisi2](https://x.com/nima2qisi2))

**입력:** 공개된 프롬프트는 참조 이미지를 요구하지 않습니다.

제작자는 GIF를 요청했습니다. X는 이 애니메이션을 MP4로 제공하므로 포스터를 누르면 원본 애니메이션이 열립니다. 공개된 프롬프트와 일치하는 백악관 클립만 수록하고 같은 게시물의 자유의 여신상 및 자금성 클립은 제외했습니다. 이 합성 회전 영상은 기록 영상이나 검증된 건축 구조를 보여주는 자료가 아닙니다.

| 결과 |
| --- |
| 원본 출처의 이미지·영상입니다. 참조 이미지와 생성 결과의 역할은 각 표기를 확인하세요. |

[![백악관 합성 회전 애니메이션](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

[제작자의 회전 애니메이션 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

**프롬프트:**

```
帮我做一个真实白宫外观的360°环绕模仿无人机拍摄，要真实还原建筑环境的实际外观情况，做成gif
```

---

<a id="gpt-image-2-6-case-252"></a>
### 사례 252: [주변 장면을 유지하며 꽃 제거](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object) (작성자 [@OpenAI](https://developers.openai.com))

**입력:** 아래에 표시된 참조 이미지를 사용하세요.

공식 편집 예시입니다. 제공된 참조 사진을 사용하세요. 공개된 두 모델의 결과를 함께 보여주며, 반복 측정한 벤치마크는 아닙니다.

| 결과 |
| --- |
| 원본 출처의 이미지·영상입니다. 참조 이미지와 생성 결과의 역할은 각 표기를 확인하세요. |

<table>
<tr><td colspan="2"><strong>참조 이미지</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-blue-hat.webp" width="360" alt="참조 사진: 꽃을 들고 있는 남성"></td></tr>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-flare.webp" width="360" alt="주변 장면을 유지하며 꽃 제거 — GPT Image 2.6 Flare"></td><td width="50%" valign="top"><strong>GPT Image 2.6 Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-sunburst.webp" width="360" alt="주변 장면을 유지하며 꽃 제거 — GPT Image 2.6 Sunburst"></td></tr>
</table>

**프롬프트:**

```
Remove the flower from man's hand. Do not change anything else.
```

---

<a id="gpt-image-2-6-case-253"></a>
### 사례 253: [눈 내리는 저녁의 광고판 편집](https://developers.openai.com/api/docs/guides/image-prompting#change-one-condition) (작성자 [@OpenAI](https://developers.openai.com))

**입력:** 아래에 표시된 참조 이미지를 사용하세요.

광고판을 처음 생성하는 프롬프트가 아니라 후속 편집 프롬프트의 전문입니다. 각 모델에 해당하는 해 질 녘 광고판 이미지를 입력으로 사용하세요. 모델별 입력과 출력을 나란히 표시했습니다.

| 결과 |
| --- |
| 원본 출처의 이미지·영상입니다. 참조 이미지와 생성 결과의 역할은 각 표기를 확인하세요. |

<table>
<tr><td width="50%" valign="top"><strong>Flare 입력</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-flare.webp" width="360" alt="눈 내리는 저녁의 광고판 편집 — Flare 입력"></td><td width="50%" valign="top"><strong>Flare 겨울 출력</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-flare.webp" width="360" alt="눈 내리는 저녁의 광고판 편집 — Flare 겨울 출력"></td></tr>
<tr><td width="50%" valign="top"><strong>Sunburst 입력</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-sunburst.webp" width="360" alt="눈 내리는 저녁의 광고판 편집 — Sunburst 입력"></td><td width="50%" valign="top"><strong>Sunburst 겨울 출력</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-sunburst.webp" width="360" alt="눈 내리는 저녁의 광고판 편집 — Sunburst 겨울 출력"></td></tr>
</table>

**프롬프트:**

```
Make it look like a winter evening with snowfall.
```

---

<a id="gpt-image-2-6-case-254"></a>
### 사례 254: [차를 든 인물 사진 버전 비교](https://x.com/v3rt0x_/status/2118147596891901957) (작성자 [@v3rt0x_](https://x.com/v3rt0x_))

**입력:** 공개된 프롬프트는 참조 이미지를 요구하지 않습니다.

제작자는 첫 이미지를 GPT Image 2.6, 두 번째 이미지를 GPT Image 2.5로 표기했습니다. 세부 모델, 설정, 재시도 횟수는 공개하지 않았습니다. 제작자의 비교이며 통제된 벤치마크는 아닙니다.

| 결과 |
| --- |
| 원본 출처의 이미지·영상입니다. 참조 이미지와 생성 결과의 역할은 각 표기를 확인하세요. |

<table>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 — 제작자 표기</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147098709274624.jpg" width="360" alt="차를 든 인물 사진 버전 비교 — GPT Image 2.6 — 제작자 표기"></td><td width="50%" valign="top"><strong>GPT Image 2.5 — 제작자 표기</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147411746955264.jpg" width="360" alt="차를 든 인물 사진 버전 비교 — GPT Image 2.5 — 제작자 표기"></td></tr>
</table>

**프롬프트:**

```
a realistic photo of a woman holding a cup of tea inside her home
```

---

<a id="gpt-image-2-6-case-255"></a>
### 사례 255: [바로크 액자의 겨울 갤러리 포스터](https://x.com/Goodmanprotocol/status/2118193088128745875) (작성자 [@Goodmanprotocol](https://x.com/Goodmanprotocol))

**입력:** 사용 권한이 있는 장면 이미지 한 장을 업로드합니다. 원본 입력 이미지는 별도로 제공되지 않았습니다.

제작자가 GPT Image 2.6 출력물이라고 밝힌 예시입니다. 두 포스터 모두 생성 결과이며 각각 작은 참조 이미지가 들어 있지만, 원본 입력 이미지는 별도로 제공되지 않았습니다. 사용 권한이 있는 자신의 장면 이미지를 업로드하세요. 모델 종류, 설정, 재시도 횟수는 공개되지 않았습니다.

| 결과 | 결과 2 |
| --- | --- |
| <strong>눈사람 갤러리 포스터</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193058370158592.jpg" width="320" alt="눈사람 갤러리 포스터"> | <strong>겨울 마을 갤러리 포스터</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193073935245312.jpg" width="320" alt="겨울 마을 갤러리 포스터"> |

**프롬프트:**

```
PREMIUM BAROQUE FRAMED ARTWORK - PHOTOREALISTIC GALLERY POSTER

Use the uploaded image as the sole visual reference. Create a seamless 3:4 vertical fine-art poster.

TOP SECTION (75%): Display the original scene as a beautiful painting inside an ornate antique gold Baroque frame, mounted on a subtly textured plaster wall. Preserve the original scene and its defining details. Select 1–3 prominent elements already present in the image and extend them beyond the frame in realistic 3D, with natural depth, perspective and cast shadows. Do not introduce any new objects, flowers, plants or decorative elements that are not present in the source image. Choose a muted wall color derived from the original image's palette. Match the lighting, atmosphere and time of day of the original scene. Photorealistic rendering with a sophisticated fine-art gallery aesthetic.

BOTTOM SECTION (25%): Continue the same plaster wall and lighting seamlessly. Place a small, clean thumbnail of the original unedited image slightly left of center, without a white border and with a subtle natural shadow. Beside it, add a refined 2–3-word ALL-CAPS serif title and a single-line italic subtitle inspired by the original scene. Keep the typography minimal, elegant and clearly contrasted against the wall.

COMPOSITION & QUALITY: The entire poster must appear as one continuous image. No divider lines, white bands, gaps, separate panels or outer borders. Ensure seamless transitions, balanced spacing, realistic materials, sophisticated typography and premium editorial art direction. Preserve the original subject's identity and visual character without altering the source scene.
```

---

<a id="gpt-image-2-6-case-256"></a>
### 사례 256: [깔끔한 캐릭터 스트레칭 애니메이션](https://x.com/MiraMusic_AI/status/2118168013618987298) (작성자 [@MiraMusic_AI](https://x.com/MiraMusic_AI))

**입력:** 사용 권한이 있는 캐릭터 참조 이미지를 준비합니다.

제작자는 캐릭터 설정화 및 생성된 애니메이션과 함께 이 일본어 애니메이션 프롬프트 전문을 공개했습니다. 사용 권한이 있는 캐릭터 참조 이미지를 사용하세요. 모델 종류, 설정, 재시도 횟수는 공개되지 않았습니다. X는 요청한 GIF를 MP4로 제공하므로 링크된 애니메이션에서 움직임을 확인할 수 있습니다.

| 입력 | 결과 |
| --- | --- |
| <strong>제작자의 캐릭터 설정화</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167991833759744.jpg" width="320" alt="제작자의 캐릭터 설정화"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4"><strong>스트레칭 애니메이션 미리보기</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.jpg" width="320" alt="스트레칭 애니메이션 미리보기"></a> |

[제작자의 스트레칭 애니메이션 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4)

**프롬프트:**

```
ストレッチをしているGIFを製作してください。
仕上げはフラットでクリーンに。
複雑な微細テクスチャ、過剰な細密描写、粒状ノイズ、ザラつき、斜めグリッド状の模様なし
```

---

<a id="gpt-image-2-6-case-257"></a>
### 사례 257: [밥 먹는 캐릭터 스티커](https://x.com/Gorden_Sun/status/2118166046175908016) (작성자 [@Gorden_Sun](https://x.com/Gorden_Sun))

**입력:** 사용 권한이 있는 캐릭터 참조 이미지를 준비합니다.

제작자는 첫 번째 첨부 파일이 생성된 GIF이고 두 번째가 캐릭터 참조 이미지라고 명시했습니다. 중국어 프롬프트는 이미지에 真香！라는 문구를 넣도록 요청합니다. 사용 권한이 있는 캐릭터 참조 이미지를 사용하세요. 모델 종류, 설정, 재시도 횟수는 공개되지 않았으며, X는 애니메이션을 MP4로 제공합니다.

| 입력 | 결과 |
| --- | --- |
| <strong>제작자의 캐릭터 참조 이미지</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118166009131757568.jpg" width="320" alt="제작자의 캐릭터 참조 이미지"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4"><strong>밥 먹는 애니메이션 미리보기</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.jpg" width="320" alt="밥 먹는 애니메이션 미리보기"></a> |

[제작자의 밥 먹는 애니메이션 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4)

**프롬프트:**

```
使用这个角色，生成一张GIF图，内容是她吃大白米饭，图片里有文字：真香！
```

---

<a id="gpt-image-2-6-case-258"></a>
### 사례 258: [원 표시로 지정하는 캐릭터 크리스마스 편집](https://x.com/IHayato/status/2118151619212890291) (작성자 [@IHayato](https://x.com/IHayato))

**입력:** 편집할 부분을 빨간 원과 파란 원으로 표시한 캐릭터 이미지를 준비합니다.

제작자가 인용한 일본어 후속 편집 프롬프트 전문입니다. 빨간 원에는 산타 모자를 추가하고 파란 원 안의 책은 선물로 바꾸라는 지시입니다. 원본 비교 이미지에는 표시된 입력과 편집 결과가 함께 있지만, 표시가 없는 입력 이미지는 별도로 제공되지 않았습니다. 직접 표시한 캐릭터 이미지를 사용하세요. 제작자는 GPT Image 2.6으로 편집했다고 밝혔지만 모델 종류는 명시하지 않았습니다.

| 결과 |
| --- |
| <strong>제작자 비교 이미지: 표시된 입력과 크리스마스 편집</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151559322419200.jpg" width="640" alt="제작자 비교 이미지: 표시된 입력과 크리스마스 편집"> |

**프롬프트:**

```
赤丸にサンタ帽、青丸の本はプレゼントに
```

---

<a id="gpt-image-2-6-case-259"></a>
### 사례 259: [눈을 깜박이며 흔들리는 캐릭터 애니메이션](https://x.com/IHayato/status/2118151619212890291) (작성자 [@IHayato](https://x.com/IHayato))

**입력:** 사용 권한이 있는 캐릭터 참조 이미지를 준비합니다.

제작자가 인용한 일본어 후속 애니메이션 프롬프트 전문입니다. 사용 권한이 있는 캐릭터 참조 이미지를 준비하세요. 이 애니메이션의 원본 입력 이미지는 별도로 제공되지 않았습니다. 같은 게시물의 별도 크리스마스 편집 및 가격표 이미지는 이 애니메이션의 입력으로 취급하지 않습니다. 제작자는 GPT Image 2.6 결과라고 밝혔지만 모델 종류는 명시하지 않았습니다. X는 애니메이션을 MP4로 제공합니다.

| 결과 |
| --- |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4"><strong>눈 깜박임 애니메이션 미리보기</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.jpg" width="320" alt="눈 깜박임 애니메이션 미리보기"></a> |

[제작자의 눈 깜박임 애니메이션 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4)

**프롬프트:**

```
まばたきして、ふわっと揺れて
```

---

<a id="gpt-image-2-6-case-260"></a>
### 사례 260: [애니메이션풍 만화경 루프 영상](https://x.com/aimikoda/status/2118665755994546650) (작성자 [@aimikoda](https://x.com/aimikoda))

**입력:** 사용 권한이 있는 캐릭터 참조 이미지를 준비합니다.

작성자는 이 애니메이션을 GPT Image 2.6으로 만들었다고 밝혔습니다. 게시물에는 애니메이션이 올라와 있으며 원본 캐릭터 참조 이미지는 공개되지 않았습니다. X는 GIF를 MP4로 제공합니다.

| 결과 |
| --- |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.mp4"><strong>애니메이션풍 만화경 영상 미리보기</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.jpg" width="320" alt="애니메이션풍 만화경 영상 미리보기"></a> |

[작성자의 만화경 애니메이션 재생](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118665679846993920.mp4)

**프롬프트:**

```
Create a seamless looping 1:1 2D anime kaleidoscope animation using the supplied character as the exact identity reference. Preserve the face, hairstyle, anatomy, outfit and visual style.

COMPOSITION: A vibrant, symmetrical kaleidoscope featuring one large central character and four surrounding copies arranged diagonally at different radial angles. Layer overlapping character portraits, decorative Japanese fans, floral motifs and colorful geometric patterns. Fill the entire frame with dense, intricate details extending beyond the edges. No circular frames.

ANIMATION: Keep the overall composition stationary while all five character instances perform independent, expressive anime movements: head tilts, blinking, playful expressions, flowing hair and rhythmic gestures. Use smooth hand-drawn animation with crisp linework, cel shading and lively secondary motion.

LOOP: All movements return naturally to their initial poses for a perfectly seamless infinite loop.

No text, logos, subtitles or additional characters.
```

---
