# GPT Image 2.6 — Новейшие примеры с промптами

[← Все 259 промптов](../../README_ru.md)

Девять полных публичных промптов: два официальных примера редактирования и семь авторских промптов для анимации, правок, постеров и сравнения версий. Исходные 250 примеров GPT Image 2.5 сохраняют свои номера.

## Содержание

  - [Пример 251: Анимация облёта Белого дома](#gpt-image-2-6-case-251)
  - [Пример 252: Удаление цветка с сохранением сцены](#gpt-image-2-6-case-252)
  - [Пример 253: Заснеженный вечер на рекламном щите](#gpt-image-2-6-case-253)
  - [Пример 254: Сравнение версий портрета с чаем](#gpt-image-2-6-case-254)
  - [Пример 255: Зимние галерейные постеры в барочной раме](#gpt-image-2-6-case-255)
  - [Пример 256: Чистая анимация потягивающегося персонажа](#gpt-image-2-6-case-256)
  - [Пример 257: Стикер с персонажем, который ест рис](#gpt-image-2-6-case-257)
  - [Пример 258: Праздничная правка персонажа по круговым меткам](#gpt-image-2-6-case-258)
  - [Пример 259: Анимация моргающего и покачивающегося персонажа](#gpt-image-2-6-case-259)

<a id="gpt-image-2-6-case-251"></a>
### Пример 251: [Анимация облёта Белого дома](https://x.com/nima2qisi2/status/2118295936606798006) (автор [@nima2qisi2](https://x.com/nima2qisi2))

**Входные материалы:** Опубликованный промпт не требует референсного изображения.

Автор запрашивает GIF. X предоставляет эту анимацию в формате MP4; превью ведёт к исходной анимации. Опубликованному промпту соответствует только ролик с Белым домом; ролики со Статуей Свободы и Запретным городом из той же публикации исключены. Этот синтетический облёт не является документальной съёмкой и не подтверждает точность архитектурной геометрии.

| Результат |
| --- |
| Медиа из источника; входные изображения и подписи моделей приведены ниже. |

[![Синтетическая анимация облёта Белого дома](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

[Воспроизвести авторскую анимацию облёта](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

**Промпт:**

```
帮我做一个真实白宫外观的360°环绕模仿无人机拍摄，要真实还原建筑环境的实际外观情况，做成gif
```

---

<a id="gpt-image-2-6-case-252"></a>
### Пример 252: [Удаление цветка с сохранением сцены](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object) (автор [@OpenAI](https://developers.openai.com))

**Входные материалы:** Используйте приведённые ниже референсные изображения.

Официальный пример редактирования. Используйте предоставленное референсное фото. Оба опубликованных результата показаны вместе; это пример, а не многократно повторённый бенчмарк.

| Результат |
| --- |
| Медиа из источника; входные изображения и подписи моделей приведены ниже. |

<table>
<tr><td colspan="2"><strong>Референс</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-blue-hat.webp" width="360" alt="Референсное фото: мужчина с цветком"></td></tr>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-flare.webp" width="360" alt="Удаление цветка с сохранением сцены — GPT Image 2.6 Flare"></td><td width="50%" valign="top"><strong>GPT Image 2.6 Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-sunburst.webp" width="360" alt="Удаление цветка с сохранением сцены — GPT Image 2.6 Sunburst"></td></tr>
</table>

**Промпт:**

```
Remove the flower from man's hand. Do not change anything else.
```

---

<a id="gpt-image-2-6-case-253"></a>
### Пример 253: [Заснеженный вечер на рекламном щите](https://developers.openai.com/api/docs/guides/image-prompting#change-one-condition) (автор [@OpenAI](https://developers.openai.com))

**Входные материалы:** Используйте приведённые ниже референсные изображения.

Это полный промпт последующей правки, а не исходного создания рекламного щита. Для каждой модели используйте соответствующее изображение щита на закате. Входные изображения и результаты каждой модели показаны рядом.

| Результат |
| --- |
| Медиа из источника; входные изображения и подписи моделей приведены ниже. |

<table>
<tr><td width="50%" valign="top"><strong>Входное изображение Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-flare.webp" width="360" alt="Заснеженный вечер на рекламном щите — Входное изображение Flare"></td><td width="50%" valign="top"><strong>Зимний результат Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-flare.webp" width="360" alt="Заснеженный вечер на рекламном щите — Зимний результат Flare"></td></tr>
<tr><td width="50%" valign="top"><strong>Входное изображение Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-sunburst.webp" width="360" alt="Заснеженный вечер на рекламном щите — Входное изображение Sunburst"></td><td width="50%" valign="top"><strong>Зимний результат Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-sunburst.webp" width="360" alt="Заснеженный вечер на рекламном щите — Зимний результат Sunburst"></td></tr>
</table>

**Промпт:**

```
Make it look like a winter evening with snowfall.
```

---

<a id="gpt-image-2-6-case-254"></a>
### Пример 254: [Сравнение версий портрета с чаем](https://x.com/v3rt0x_/status/2118147596891901957) (автор [@v3rt0x_](https://x.com/v3rt0x_))

**Входные материалы:** Опубликованный промпт не требует референсного изображения.

Автор обозначил первое изображение как GPT Image 2.6, а второе — как GPT Image 2.5. Вариант модели, настройки и повторные попытки не раскрыты. Это авторское сравнение, а не контролируемый бенчмарк.

| Результат |
| --- |
| Медиа из источника; входные изображения и подписи моделей приведены ниже. |

<table>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 — обозначение автора</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147098709274624.jpg" width="360" alt="Сравнение версий портрета с чаем — GPT Image 2.6 — обозначение автора"></td><td width="50%" valign="top"><strong>GPT Image 2.5 — обозначение автора</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147411746955264.jpg" width="360" alt="Сравнение версий портрета с чаем — GPT Image 2.5 — обозначение автора"></td></tr>
</table>

**Промпт:**

```
a realistic photo of a woman holding a cup of tea inside her home
```

---

<a id="gpt-image-2-6-case-255"></a>
### Пример 255: [Зимние галерейные постеры в барочной раме](https://x.com/Goodmanprotocol/status/2118193088128745875) (автор [@Goodmanprotocol](https://x.com/Goodmanprotocol))

**Входные материалы:** Загрузите изображение сцены, на использование которого у вас есть разрешение; отдельные исходные изображения не предоставлены.

Автор относит эти результаты к GPT Image 2.6. Оба постера — результаты генерации, каждый содержит маленькую миниатюру референса; отдельные исходные изображения не предоставлены. Загрузите собственное изображение сцены, на использование которого у вас есть разрешение. Вариант модели, настройки и повторные попытки не раскрыты.

| Результат | Результат 2 |
| --- | --- |
| <strong>Галерейный постер со снеговиком</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193058370158592.jpg" width="320" alt="Галерейный постер со снеговиком"> | <strong>Галерейный постер с зимней деревней</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193073935245312.jpg" width="320" alt="Галерейный постер с зимней деревней"> |

**Промпт:**

```
PREMIUM BAROQUE FRAMED ARTWORK - PHOTOREALISTIC GALLERY POSTER

Use the uploaded image as the sole visual reference. Create a seamless 3:4 vertical fine-art poster.

TOP SECTION (75%): Display the original scene as a beautiful painting inside an ornate antique gold Baroque frame, mounted on a subtly textured plaster wall. Preserve the original scene and its defining details. Select 1–3 prominent elements already present in the image and extend them beyond the frame in realistic 3D, with natural depth, perspective and cast shadows. Do not introduce any new objects, flowers, plants or decorative elements that are not present in the source image. Choose a muted wall color derived from the original image's palette. Match the lighting, atmosphere and time of day of the original scene. Photorealistic rendering with a sophisticated fine-art gallery aesthetic.

BOTTOM SECTION (25%): Continue the same plaster wall and lighting seamlessly. Place a small, clean thumbnail of the original unedited image slightly left of center, without a white border and with a subtle natural shadow. Beside it, add a refined 2–3-word ALL-CAPS serif title and a single-line italic subtitle inspired by the original scene. Keep the typography minimal, elegant and clearly contrasted against the wall.

COMPOSITION & QUALITY: The entire poster must appear as one continuous image. No divider lines, white bands, gaps, separate panels or outer borders. Ensure seamless transitions, balanced spacing, realistic materials, sophisticated typography and premium editorial art direction. Preserve the original subject's identity and visual character without altering the source scene.
```

---

<a id="gpt-image-2-6-case-256"></a>
### Пример 256: [Чистая анимация потягивающегося персонажа](https://x.com/MiraMusic_AI/status/2118168013618987298) (автор [@MiraMusic_AI](https://x.com/MiraMusic_AI))

**Входные материалы:** Используйте референс персонажа, на использование которого у вас есть разрешение.

Автор публикует этот полный японский промпт для анимации вместе с листом персонажа и полученной анимацией. Используйте референс персонажа, на использование которого у вас есть разрешение. Вариант модели, настройки и повторные попытки не раскрыты. X отдаёт запрошенный GIF в формате MP4; откройте анимацию по ссылке, чтобы увидеть движение.

| Входные материалы | Результат |
| --- | --- |
| <strong>Лист персонажа автора</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167991833759744.jpg" width="320" alt="Лист персонажа автора"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4"><strong>Кадр анимации потягивания</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.jpg" width="320" alt="Кадр анимации потягивания"></a> |

[Воспроизвести анимацию потягивания автора](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4)

**Промпт:**

```
ストレッチをしているGIFを製作してください。
仕上げはフラットでクリーンに。
複雑な微細テクスチャ、過剰な細密描写、粒状ノイズ、ザラつき、斜めグリッド状の模様なし
```

---

<a id="gpt-image-2-6-case-257"></a>
### Пример 257: [Стикер с персонажем, который ест рис](https://x.com/Gorden_Sun/status/2118166046175908016) (автор [@Gorden_Sun](https://x.com/Gorden_Sun))

**Входные материалы:** Используйте референс персонажа, на использование которого у вас есть разрешение.

Автор прямо указывает, что первое вложение — созданный GIF, а второе — референс персонажа. Китайский промпт требует надпись 真香！ на изображении. Используйте референс персонажа, на использование которого у вас есть разрешение. Вариант модели, настройки и повторные попытки не раскрыты; X отдаёт анимацию в формате MP4.

| Входные материалы | Результат |
| --- | --- |
| <strong>Референс персонажа автора</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118166009131757568.jpg" width="320" alt="Референс персонажа автора"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4"><strong>Кадр анимации с миской риса</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.jpg" width="320" alt="Кадр анимации с миской риса"></a> |

[Воспроизвести анимацию автора с миской риса](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4)

**Промпт:**

```
使用这个角色，生成一张GIF图，内容是她吃大白米饭，图片里有文字：真香！
```

---

<a id="gpt-image-2-6-case-258"></a>
### Пример 258: [Праздничная правка персонажа по круговым меткам](https://x.com/IHayato/status/2118151619212890291) (автор [@IHayato](https://x.com/IHayato))

**Входные материалы:** Предоставьте изображение персонажа с красными и синими метками, обозначающими нужные правки.

Это полный японский промпт для последующей правки, процитированный автором: добавить шапку Санты в красном круге и заменить книгу в синем круге подарком. Исходный коллаж показывает вместе размеченное входное изображение и результат правки; отдельное изображение без разметки не предоставлено. Используйте собственное размеченное изображение персонажа. Автор относит правку к GPT Image 2.6, не называя вариант модели.

| Результат |
| --- |
| <strong>Коллаж автора: размеченный вход и праздничная правка</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151559322419200.jpg" width="640" alt="Коллаж автора: размеченный вход и праздничная правка"> |

**Промпт:**

```
赤丸にサンタ帽、青丸の本はプレゼントに
```

---

<a id="gpt-image-2-6-case-259"></a>
### Пример 259: [Анимация моргающего и покачивающегося персонажа](https://x.com/IHayato/status/2118151619212890291) (автор [@IHayato](https://x.com/IHayato))

**Входные материалы:** Используйте референс персонажа, на использование которого у вас есть разрешение.

Это полный японский промпт для последующей анимации, процитированный автором. Предоставьте референс персонажа, на использование которого у вас есть разрешение; отдельное входное изображение для этой анимации не предоставлено. Публикация также содержит отдельную праздничную правку и график цен; ни один из них здесь не используется как вход для анимации. Автор относит результат к GPT Image 2.6, не называя вариант модели. X отдаёт анимацию в формате MP4.

| Результат |
| --- |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4"><strong>Кадр анимации моргающего персонажа</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.jpg" width="320" alt="Кадр анимации моргающего персонажа"></a> |

[Воспроизвести анимацию моргания автора](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4)

**Промпт:**

```
まばたきして、ふわっと揺れて
```

---
