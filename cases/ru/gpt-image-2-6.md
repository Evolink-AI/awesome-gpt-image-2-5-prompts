# GPT Image 2.6 — Новейшие примеры с промптами

[← Все 254 промпта](../../README_ru.md)

Четыре полных публичных промпта: два официальных примера редактирования, авторская анимация и авторское сравнение версий. Исходные 250 примеров GPT Image 2.5 сохраняют свои номера.

## Содержание

  - [Пример 251: Анимация облёта Белого дома](#gpt-image-2-6-case-251)
  - [Пример 252: Удаление цветка с сохранением сцены](#gpt-image-2-6-case-252)
  - [Пример 253: Заснеженный вечер на рекламном щите](#gpt-image-2-6-case-253)
  - [Пример 254: Сравнение версий портрета с чаем](#gpt-image-2-6-case-254)

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
