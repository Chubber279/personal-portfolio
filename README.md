# Portfolio, Resume and CV — Lorenzo Miguel Ocampo

One data file drives three outputs: the one-page portfolio site, the 1-page resume and the 2-page
CV. Edit `src/content.py`, run the build, and every output changes together.

Facts come from the knowledge base (`Desktop/profile-knowledge-base`). Do not add claims or metrics
that are not recorded there; `credentials/Credentials.md` says what may be printed.

## Files

| File | Purpose |
|---|---|
| `src/content.py` | **Single source of truth**: contact, summary, skills, experience, projects, education, publication, plus website-only copy (`SITE`) |
| `src/build.py` | Entry point: builds everything below |
| `src/documents.py` | Resume/CV as `.md`, `.docx` and `.pdf` |
| `src/webpage.py`, `src/template.html` | Website renderer and page shell |
| `index.html` | Generated website (GitHub Pages root) — do not hand-edit |
| `documents/` | Generated `Lorenzo_Ocampo_Resume_2026.*` and `Lorenzo_Ocampo_CV_2026.*`; the site links the PDFs |
| `styles.css` | Layout and monochrome theme (black/grey/white; Cormorant Garamond display + Inter text from Google Fonts, system serif/sans fallbacks). Light/dark follows the system; toggle overrides and is saved |
| `script.js` | Theme toggle, mobile menu, scroll effects, footer year |
| `assets/favicon.svg` | Site icon |

## Build

```
pip install python-docx docx2pdf
python src/build.py            # site + resume/CV (.md, .docx, .pdf)
python src/build.py --no-pdf   # skip the PDF export
```

The PDF export drives Microsoft Word through `docx2pdf`. After a build, check that the resume
still fits on 1 page and the CV on 2.

## Preview locally

```
npx serve .
```

or open `index.html` directly in a browser.

## Publishing (free)

GitHub account: https://github.com/Chubber279. The account already has a repository named
`Chubber279.github.io` (a 2021 class exercise page), so the cleanest URL is to publish there:

1. Back up or archive the current contents of `Chubber279.github.io` if you want to keep them.
2. Replace its contents with this folder and push to `main`:
   `git remote add origin https://github.com/Chubber279/Chubber279.github.io.git`
   `git push -f origin master:main` (overwrites the old page — step 1 first).
3. Repository Settings → Pages → Deploy from branch → `main` / root.
4. The site goes live at `https://chubber279.github.io/`.

Alternatives: a new repository `portfolio` (URL `https://chubber279.github.io/portfolio/`), or
Netlify / Cloudflare Pages (drag-and-drop this folder).

After publishing, add the URL to `LINKS` in `src/content.py` (then rebuild), the knowledge-base
credentials register, and LinkedIn.

## Next improvements

- Add screenshots or short demos of the Retail Sales & Inventory Site (demo mode, `Start Demo.bat`,
  uses generated data) and the Staff Scheduling Application (redact store names and data).
- Publish sanitized source for the Staff Scheduling Application on GitHub and link it from its card.
  The Retail Sales & Inventory Site stays private (client data); keep the client's name off every
  output.
- Add outcome metrics for the project-management scope once available.
