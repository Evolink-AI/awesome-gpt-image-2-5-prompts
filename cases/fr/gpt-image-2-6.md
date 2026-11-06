# GPT Image 2.6 — Nouveaux cas avec prompt

[← Les 259 prompts](../../README_fr.md)

Neuf prompts publics complets : deux exemples officiels de retouche et sept prompts attribués à des créateurs couvrant l’animation, la retouche, les affiches et une comparaison de versions. Les 250 cas originaux de GPT Image 2.5 conservent leurs numéros.

## Sommaire

  - [Cas 251: Animation en orbite autour de la Maison-Blanche](#gpt-image-2-6-case-251)
  - [Cas 252: Suppression d’une fleur en préservant la scène](#gpt-image-2-6-case-252)
  - [Cas 253: Retouche d’un panneau publicitaire par soirée enneigée](#gpt-image-2-6-case-253)
  - [Cas 254: Comparaison de versions : portrait avec une tasse de thé](#gpt-image-2-6-case-254)
  - [Cas 255: Affiches hivernales à cadre baroque](#gpt-image-2-6-case-255)
  - [Cas 256: Animation épurée d’un personnage qui s’étire](#gpt-image-2-6-case-256)
  - [Cas 257: Autocollant de personnage mangeant du riz](#gpt-image-2-6-case-257)
  - [Cas 258: Retouche festive de personnage guidée par des cercles](#gpt-image-2-6-case-258)
  - [Cas 259: Animation de personnage clignant des yeux et se balançant](#gpt-image-2-6-case-259)

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

<a id="gpt-image-2-6-case-255"></a>
### Cas 255: [Affiches hivernales à cadre baroque](https://x.com/Goodmanprotocol/status/2118193088128745875) (par [@Goodmanprotocol](https://x.com/Goodmanprotocol))

**Entrée:** Importez une image de scène que vous avez le droit d’utiliser ; les images originales ne sont pas fournies séparément.

Le créateur attribue ces résultats à GPT Image 2.6. Les deux affiches sont des résultats et comportent chacune une petite vignette de référence ; les images originales ne sont pas fournies séparément. Importez votre propre image de scène que vous avez le droit d’utiliser. La variante, les réglages et les nouvelles tentatives ne sont pas précisés.

| Résultat | Résultat 2 |
| --- | --- |
| <strong>Affiche de galerie au bonhomme de neige</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193058370158592.jpg" width="320" alt="Affiche de galerie au bonhomme de neige"> | <strong>Affiche de galerie au village hivernal</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118193073935245312.jpg" width="320" alt="Affiche de galerie au village hivernal"> |

**Prompt:**

```
PREMIUM BAROQUE FRAMED ARTWORK - PHOTOREALISTIC GALLERY POSTER

Use the uploaded image as the sole visual reference. Create a seamless 3:4 vertical fine-art poster.

TOP SECTION (75%): Display the original scene as a beautiful painting inside an ornate antique gold Baroque frame, mounted on a subtly textured plaster wall. Preserve the original scene and its defining details. Select 1–3 prominent elements already present in the image and extend them beyond the frame in realistic 3D, with natural depth, perspective and cast shadows. Do not introduce any new objects, flowers, plants or decorative elements that are not present in the source image. Choose a muted wall color derived from the original image's palette. Match the lighting, atmosphere and time of day of the original scene. Photorealistic rendering with a sophisticated fine-art gallery aesthetic.

BOTTOM SECTION (25%): Continue the same plaster wall and lighting seamlessly. Place a small, clean thumbnail of the original unedited image slightly left of center, without a white border and with a subtle natural shadow. Beside it, add a refined 2–3-word ALL-CAPS serif title and a single-line italic subtitle inspired by the original scene. Keep the typography minimal, elegant and clearly contrasted against the wall.

COMPOSITION & QUALITY: The entire poster must appear as one continuous image. No divider lines, white bands, gaps, separate panels or outer borders. Ensure seamless transitions, balanced spacing, realistic materials, sophisticated typography and premium editorial art direction. Preserve the original subject's identity and visual character without altering the source scene.
```

---

<a id="gpt-image-2-6-case-256"></a>
### Cas 256: [Animation épurée d’un personnage qui s’étire](https://x.com/MiraMusic_AI/status/2118168013618987298) (par [@MiraMusic_AI](https://x.com/MiraMusic_AI))

**Entrée:** Utilisez une référence de personnage que vous avez le droit d’utiliser.

Le créateur publie ce prompt d’animation complet en japonais avec une fiche de personnage et l’animation obtenue. Utilisez une référence de personnage que vous avez le droit d’utiliser. La variante, les réglages et les nouvelles tentatives ne sont pas précisés. X diffuse le GIF demandé au format MP4 ; ouvrez l’animation liée pour voir le mouvement.

| Entrée | Résultat |
| --- | --- |
| <strong>Fiche de personnage du créateur</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167991833759744.jpg" width="320" alt="Fiche de personnage du créateur"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4"><strong>Aperçu de l’animation d’étirement</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.jpg" width="320" alt="Aperçu de l’animation d’étirement"></a> |

[Lire l’animation d’étirement du créateur](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118167499812536321.mp4)

**Prompt:**

```
ストレッチをしているGIFを製作してください。
仕上げはフラットでクリーンに。
複雑な微細テクスチャ、過剰な細密描写、粒状ノイズ、ザラつき、斜めグリッド状の模様なし
```

---

<a id="gpt-image-2-6-case-257"></a>
### Cas 257: [Autocollant de personnage mangeant du riz](https://x.com/Gorden_Sun/status/2118166046175908016) (par [@Gorden_Sun](https://x.com/Gorden_Sun))

**Entrée:** Utilisez une référence de personnage que vous avez le droit d’utiliser.

Le créateur indique explicitement que la première pièce jointe est le GIF généré et la seconde sa référence de personnage. Le prompt en chinois demande le texte 真香！ dans l’image. Utilisez une référence de personnage que vous avez le droit d’utiliser. La variante, les réglages et les nouvelles tentatives ne sont pas précisés ; X diffuse l’animation au format MP4.

| Entrée | Résultat |
| --- | --- |
| <strong>Référence de personnage du créateur</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118166009131757568.jpg" width="320" alt="Référence de personnage du créateur"> | <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4"><strong>Aperçu de l’animation avec un bol de riz</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.jpg" width="320" alt="Aperçu de l’animation avec un bol de riz"></a> |

[Lire l’animation du créateur avec un bol de riz](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118165970133168129.mp4)

**Prompt:**

```
使用这个角色，生成一张GIF图，内容是她吃大白米饭，图片里有文字：真香！
```

---

<a id="gpt-image-2-6-case-258"></a>
### Cas 258: [Retouche festive de personnage guidée par des cercles](https://x.com/IHayato/status/2118151619212890291) (par [@IHayato](https://x.com/IHayato))

**Entrée:** Fournissez une image de personnage avec des marques rouges et bleues indiquant les retouches souhaitées.

Voici le prompt complet de retouche successive en japonais cité par le créateur : ajouter un bonnet de Père Noël dans le cercle rouge et remplacer le livre dans le cercle bleu par un cadeau. Le montage source montre ensemble l’entrée annotée et le résultat retouché ; aucune entrée sans annotation n’est fournie séparément. Utilisez votre propre image de personnage annotée. Le créateur attribue la retouche à GPT Image 2.6 sans préciser la variante.

| Résultat |
| --- |
| <strong>Montage du créateur : entrée annotée et retouche festive</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151559322419200.jpg" width="640" alt="Montage du créateur : entrée annotée et retouche festive"> |

**Prompt:**

```
赤丸にサンタ帽、青丸の本はプレゼントに
```

---

<a id="gpt-image-2-6-case-259"></a>
### Cas 259: [Animation de personnage clignant des yeux et se balançant](https://x.com/IHayato/status/2118151619212890291) (par [@IHayato](https://x.com/IHayato))

**Entrée:** Utilisez une référence de personnage que vous avez le droit d’utiliser.

Voici le prompt complet d’animation successive en japonais cité par le créateur. Fournissez une référence de personnage que vous avez le droit d’utiliser ; l’image d’entrée indépendante de cette animation n’est pas fournie. La publication contient aussi une retouche festive et un graphique de tarifs distincts ; aucun n’est utilisé ici comme entrée de l’animation. Le créateur attribue le résultat à GPT Image 2.6 sans préciser la variante. X diffuse l’animation au format MP4.

| Résultat |
| --- |
| <a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4"><strong>Aperçu du personnage qui cligne des yeux</strong><br><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.jpg" width="320" alt="Aperçu du personnage qui cligne des yeux"></a> |

[Lire l’animation de clignement du créateur](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-gpt-image-2-5-prompts/assets/gpt-image-2-6/2118151194552180736.mp4)

**Prompt:**

```
まばたきして、ふわっと揺れて
```

---
