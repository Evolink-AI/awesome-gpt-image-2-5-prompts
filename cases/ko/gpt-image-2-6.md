# GPT Image 2.6 — 최신 프롬프트 사례

[← 전체 프롬프트 254개](../../README_ko.md)

전문이 공개된 프롬프트 4개입니다. 공식 편집 예시 2개, 제작자의 애니메이션 1개, 제작자의 버전 비교 1개를 수록했습니다. 기존 GPT Image 2.5 사례 250개는 원래 번호를 유지합니다.

## 목차

  - [사례 251: 백악관 주위 회전 애니메이션](#gpt-image-2-6-case-251)
  - [사례 252: 주변 장면을 유지하며 꽃 제거](#gpt-image-2-6-case-252)
  - [사례 253: 눈 내리는 저녁의 광고판 편집](#gpt-image-2-6-case-253)
  - [사례 254: 차를 든 인물 사진 버전 비교](#gpt-image-2-6-case-254)

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
