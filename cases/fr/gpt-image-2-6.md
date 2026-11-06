# GPT Image 2.6 — Nouveaux cas avec prompt

[← Les 254 prompts](../../README_fr.md)

Quatre prompts publics complets : deux exemples officiels de retouche, une animation de créateur et une comparaison de versions publiée par un créateur. Les 250 cas originaux de GPT Image 2.5 conservent leurs numéros.

## Sommaire

  - [Cas 251: Animation en orbite autour de la Maison-Blanche](#gpt-image-2-6-case-251)
  - [Cas 252: Suppression d’une fleur en préservant la scène](#gpt-image-2-6-case-252)
  - [Cas 253: Retouche d’un panneau publicitaire par soirée enneigée](#gpt-image-2-6-case-253)
  - [Cas 254: Comparaison de versions : portrait avec une tasse de thé](#gpt-image-2-6-case-254)

<a id="gpt-image-2-6-case-251"></a>
### Cas 251: [Animation en orbite autour de la Maison-Blanche](https://x.com/nima2qisi2/status/2118295936606798006) (par [@nima2qisi2](https://x.com/nima2qisi2))

**Entrée :** Le prompt publié ne nécessite pas d’image de référence.

Le créateur demande un GIF. X diffuse cette animation au format MP4 ; l’image d’aperçu renvoie vers l’animation d’origine. Seul le clip de la Maison-Blanche correspond au prompt publié ; les clips de la statue de la Liberté et de la Cité interdite de la même publication sont exclus. Cette orbite synthétique n’est ni une vidéo documentaire ni une représentation vérifiée de la géométrie architecturale.

| Résultat |
| --- |
| Médias publiés dans la source |

[![Animation synthétique en orbite autour de la Maison-Blanche](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

[Lire l’animation en orbite du créateur](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118295303778615296.mp4)

**Prompt:**

```
帮我做一个真实白宫外观的360°环绕模仿无人机拍摄，要真实还原建筑环境的实际外观情况，做成gif
```

---

<a id="gpt-image-2-6-case-252"></a>
### Cas 252: [Suppression d’une fleur en préservant la scène](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object) (par [@OpenAI](https://developers.openai.com))

**Entrée :** Utilisez les images de référence présentées ci-dessous.

Exemple officiel de retouche. Utilisez la photographie de référence fournie. Les deux résultats publiés sont présentés ensemble ; il s’agit d’un exemple, pas d’un test répété.

| Résultat |
| --- |
| Médias publiés dans la source |

<table>
<tr><td colspan="2"><strong>Référence</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-blue-hat.webp" width="360" alt="Photographie de référence : un homme tenant une fleur"></td></tr>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-flare.webp" width="360" alt="Suppression d’une fleur en préservant la scène — GPT Image 2.6 Flare"></td><td width="50%" valign="top"><strong>GPT Image 2.6 Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/man-with-no-flower-gpt-image-2-6-sunburst.webp" width="360" alt="Suppression d’une fleur en préservant la scène — GPT Image 2.6 Sunburst"></td></tr>
</table>

**Prompt:**

```
Remove the flower from man's hand. Do not change anything else.
```

---

<a id="gpt-image-2-6-case-253"></a>
### Cas 253: [Retouche d’un panneau publicitaire par soirée enneigée](https://developers.openai.com/api/docs/guides/image-prompting#change-one-condition) (par [@OpenAI](https://developers.openai.com))

**Entrée :** Utilisez les images de référence présentées ci-dessous.

Il s’agit du prompt complet de retouche ultérieure, et non du prompt initial de génération du panneau publicitaire. Utilisez le panneau correspondant au coucher du soleil comme entrée pour chaque modèle. Les entrées et les résultats propres à chaque modèle sont présentés côte à côte.

| Résultat |
| --- |
| Médias publiés dans la source |

<table>
<tr><td width="50%" valign="top"><strong>Entrée de Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-flare.webp" width="360" alt="Retouche d’un panneau publicitaire par soirée enneigée — Entrée de Flare"></td><td width="50%" valign="top"><strong>Résultat hivernal de Flare</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-flare.webp" width="360" alt="Retouche d’un panneau publicitaire par soirée enneigée — Résultat hivernal de Flare"></td></tr>
<tr><td width="50%" valign="top"><strong>Entrée de Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-gpt-image-2-6-sunburst.webp" width="360" alt="Retouche d’un panneau publicitaire par soirée enneigée — Entrée de Sunburst"></td><td width="50%" valign="top"><strong>Résultat hivernal de Sunburst</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/billboard-winter-gpt-image-2-6-sunburst.webp" width="360" alt="Retouche d’un panneau publicitaire par soirée enneigée — Résultat hivernal de Sunburst"></td></tr>
</table>

**Prompt:**

```
Make it look like a winter evening with snowfall.
```

---

<a id="gpt-image-2-6-case-254"></a>
### Cas 254: [Comparaison de versions : portrait avec une tasse de thé](https://x.com/v3rt0x_/status/2118147596891901957) (par [@v3rt0x_](https://x.com/v3rt0x_))

**Entrée :** Le prompt publié ne nécessite pas d’image de référence.

Le créateur indique GPT Image 2.6 pour la première image et GPT Image 2.5 pour la seconde. La variante, les réglages et les nouvelles tentatives ne sont pas précisés. Il s’agit d’une comparaison de créateur, pas d’un test contrôlé.

| Résultat |
| --- |
| Médias publiés dans la source |

<table>
<tr><td width="50%" valign="top"><strong>GPT Image 2.6 — indication du créateur</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147098709274624.jpg" width="360" alt="Comparaison de versions : portrait avec une tasse de thé — GPT Image 2.6 — indication du créateur"></td><td width="50%" valign="top"><strong>GPT Image 2.5 — indication du créateur</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118147411746955264.jpg" width="360" alt="Comparaison de versions : portrait avec une tasse de thé — GPT Image 2.5 — indication du créateur"></td></tr>
</table>

**Prompt:**

```
a realistic photo of a woman holding a cup of tea inside her home
```

---
