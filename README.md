# Portfolio — Lorenzo Miguel Ocampo

Static one-page portfolio (HTML/CSS/JS, no build step). Content is sourced from
`Desktop/profile-knowledge-base`. Do not add claims that are not recorded there.

## Files

| File | Purpose |
|---|---|
| `index.html` | All content: hero, about, selected work, experience, research, skills, contact |
| `styles.css` | Layout and theme (light/dark follows the system; toggle overrides and is saved) |
| `script.js` | Theme toggle and footer year |
| `assets/Lorenzo_Ocampo_Resume_2026.pdf` | Downloadable resume — copy of `Application Documents/Lorenzo_Ocampo_Resume_2026.pdf` |
| `assets/favicon.svg` | Site icon |

## Preview locally

```
npx serve .
```

or open `index.html` directly in a browser.

## Updating

- When the resume is regenerated (`profile-knowledge-base/resume/build/build_resume.py`), copy the
  new PDF over `assets/Lorenzo_Ocampo_Resume_2026.pdf`.
- Keep wording in step with `profile-knowledge-base/resume/Resume_Remote.md`.

## Publishing (free)

1. Create a GitHub account and a public repository (e.g. `portfolio`).
2. Push this folder to it.
3. Repository Settings → Pages → Deploy from branch → `main` / root.
4. The site goes live at `https://<username>.github.io/portfolio/`.

Alternatives: Netlify or Cloudflare Pages (drag-and-drop this folder).

After publishing, add the URL to the resume header (`LINKEDIN`/contact data in
`build_resume.py`), the knowledge-base credentials register, and LinkedIn.

## Next improvements

- Add screenshots or short demos of the Retail Analytics Pipeline and Staff Scheduling Application
  (redact store names and data).
- Publish sanitized source for the two side projects on GitHub and link them from the cards.
- Add outcome metrics for the project-management scope once available.
