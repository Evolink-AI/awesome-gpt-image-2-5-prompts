# GPT Image 2.6 — Casos nuevos con prompt

[← Los 254 prompts](../../README_es.md)

Cuatro prompts públicos completos: dos ejemplos oficiales de edición, una animación de un creador y una comparación de versiones publicada por un creador. Los 250 casos originales de GPT Image 2.5 conservan sus números.

## Índice

  - [Caso 251: Animación orbital de la Casa Blanca](#gpt-image-2-6-case-251)
  - [Caso 252: Eliminación de una flor conservando la escena](#gpt-image-2-6-case-252)
  - [Caso 253: Edición de una valla publicitaria en una tarde nevada](#gpt-image-2-6-case-253)
  - [Caso 254: Comparación de versiones: retrato con té](#gpt-image-2-6-case-254)

<a id="gpt-image-2-6-case-251"></a>
### Caso 251: [Animación orbital de la Casa Blanca](https://x.com/nima2qisi2/status/2118295936606798006) (por [@nima2qisi2](https://x.com/nima2qisi2))

**Entrada:** El prompt publicado no requiere ninguna imagen de referencia.

El creador pide un GIF. X sirve esta animación en formato MP4; la imagen de vista previa enlaza a esa animación original. Solo el clip de la Casa Blanca corresponde al prompt publicado; se excluyen los clips de la Estatua de la Libertad y la Ciudad Prohibida de la misma publicación. Esta órbita sintética no es metraje documental ni una representación verificada de la geometría arquitectónica.

| Resultado |
| --- |
| Contenido multimedia publicado en la fuente |

[![Animación sintética de una órbita de la Casa Blanca](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

[Reproducir la animación orbital del creador](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

**Prompt:**

```
帮我做一个真实白宫外观的360°环绕模仿无人机拍摄，要真实还原建筑环境的实际外观情况，做成gif
```

---

<a id="gpt-image-2-6-case-252"></a>
### Caso 252: [Eliminación de una flor conservando la escena](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object) (por [@OpenAI](https://developers.openai.com))

**Entrada:** Utiliza las imágenes de referencia que aparecen a continuación.

Ejemplo oficial de edición. Utiliza la fotografía de referencia proporcionada. Los dos resultados publicados se muestran juntos; se trata de un ejemplo, no de una prueba repetida.

| Resultado |
| --- |
| Contenido multimedia publicado en la fuente |

<table>
<tr><td colspan="2"><strong>Referencia</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-blue-hat.webp" width="360" alt="Fotografía de referencia: un hombre sostiene una flor"></td></tr>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-flare.webp" width="360" alt="Eliminación de una flor conservando la escena — GPT Image 2.6 Flare"></td><td width="50%" valign="top"><strong>GPT Image 2.6 Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-sunburst.webp" width="360" alt="Eliminación de una flor conservando la escena — GPT Image 2.6 Sunburst"></td></tr>
</table>

**Prompt:**

```
Remove the flower from man's hand. Do not change anything else.
```

---

<a id="gpt-image-2-6-case-253"></a>
### Caso 253: [Edición de una valla publicitaria en una tarde nevada](https://developers.openai.com/api/docs/guides/image-prompting#change-one-condition) (por [@OpenAI](https://developers.openai.com))

**Entrada:** Utiliza las imágenes de referencia que aparecen a continuación.

Este es el prompt completo de la edición posterior, no el prompt inicial para generar la valla publicitaria. Utiliza como entrada de cada modelo su valla correspondiente al atardecer. Las entradas y los resultados de cada modelo se muestran uno al lado del otro.

| Resultado |
| --- |
| Contenido multimedia publicado en la fuente |

<table>
<tr><td width="50%" valign="top"><strong>Entrada de Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-flare.webp" width="360" alt="Edición de una valla publicitaria en una tarde nevada — Entrada de Flare"></td><td width="50%" valign="top"><strong>Resultado invernal de Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-flare.webp" width="360" alt="Edición de una valla publicitaria en una tarde nevada — Resultado invernal de Flare"></td></tr>
<tr><td width="50%" valign="top"><strong>Entrada de Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-sunburst.webp" width="360" alt="Edición de una valla publicitaria en una tarde nevada — Entrada de Sunburst"></td><td width="50%" valign="top"><strong>Resultado invernal de Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-sunburst.webp" width="360" alt="Edición de una valla publicitaria en una tarde nevada — Resultado invernal de Sunburst"></td></tr>
</table>

**Prompt:**

```
Make it look like a winter evening with snowfall.
```

---

<a id="gpt-image-2-6-case-254"></a>
### Caso 254: [Comparación de versiones: retrato con té](https://x.com/v3rt0x_/status/2118147596891901957) (por [@v3rt0x_](https://x.com/v3rt0x_))

**Entrada:** El prompt publicado no requiere ninguna imagen de referencia.

El creador identifica la primera imagen como GPT Image 2.6 y la segunda como GPT Image 2.5. No indica la variante, los ajustes ni los reintentos. Es una comparación de un creador, no una prueba controlada.

| Resultado |
| --- |
| Contenido multimedia publicado en la fuente |

<table>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 — etiqueta del creador</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147098709274624.jpg" width="360" alt="Comparación de versiones: retrato con té — GPT Image 2.6 — etiqueta del creador"></td><td width="50%" valign="top"><strong>GPT Image 2.5 — etiqueta del creador</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147411746955264.jpg" width="360" alt="Comparación de versiones: retrato con té — GPT Image 2.5 — etiqueta del creador"></td></tr>
</table>

**Prompt:**

```
a realistic photo of a woman holding a cup of tea inside her home
```

---
