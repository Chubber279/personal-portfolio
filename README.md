# Lorenzo Miguel Ocampo — Portfolio

Personal site, resume and CV for a full stack software engineer.

**Live:** https://chubber279.github.io/personal-portfolio/

<details>
<summary>Build and preview</summary>

One data file, `src/content.py`, drives the site, the 1-page resume and the 2-page CV. Edit it, then
rebuild:

```
pip install python-docx docx2pdf
python src/build.py            # site + resume/CV (.md, .docx, .pdf)
python src/build.py --no-pdf   # skip the PDF export
```

The PDF export drives Microsoft Word through `docx2pdf`. After a build, check that the resume still
fits on 1 page and the CV on 2.

Preview with `npx serve .`, or open `index.html` directly.

</details>

<details>
<summary>Files</summary>

| File | Purpose |
|---|---|
| `src/content.py` | Single source of truth for every output; its docstring holds the content and writing rules |
| `src/build.py` | Entry point: builds everything below |
| `src/documents.py` | Resume/CV as `.md`, `.docx` and `.pdf` |
| `src/webpage.py`, `src/template.html` | Website renderer and page shell |
| `index.html` | Generated website — do not hand-edit |
| `documents/` | Generated resume and CV; the site links the PDFs |
| `styles.css` | Layout and theme (warm ivory/ink, single bronze accent; Instrument Serif + Geist from Google Fonts). Light/dark follows the system; the toggle overrides and is saved |
| `script.js` | Theme toggle, mobile menu, scroll effects, footer year |
| `assets/favicon.svg` | Site icon |
| `assets/og-image.png` | 1200×630 link-preview image; referenced by absolute URL from `SITE["url"]` in `src/content.py` |

</details>
