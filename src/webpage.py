"""Render index.html from content.py and template.html."""
from __future__ import annotations

import datetime as dt
import json
import re
from html import escape
from pathlib import Path
from string import Template

import content as c

TEMPLATE = Path(__file__).with_name("template.html")


def fmt(text: str) -> str:
    """Escape text and turn **bold** into <strong>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escape(text))


def chips(items: list[str]) -> str:
    return "".join(f"<li>{escape(i)}</li>" for i in items)


def indent(lines: list[str], n: int) -> str:
    pad = " " * n
    return "\n".join(pad + line for line in lines)


def _work_card(w: dict) -> list[str]:
    if w["kind"] == "side":
        pr = next(p for p in c.PROJECTS if p["name"] == w["project"])
        badge, where, title, stack = "Side project", "", pr["name"], pr["tech"]
    else:
        badge, where, title, stack = "Production", w["where"], w["title"], w["stack"]
    metric = f'  <p class="metric">{fmt(w["metric"])}</p>' if w.get("metric") else None
    rows = "".join(f"<div><dt>{escape(k)}</dt><dd>{fmt(v)}</dd></div>" for k, v in w["rows"])
    return [
        '<article class="card reveal">',
        f'  <p class="card-tag"><span class="badge {w["kind"]}">{badge}</span>{escape(where)}</p>',
        f"  <h3>{escape(title)}</h3>",
        *([metric] if metric else []),
        f"  <dl>{rows}</dl>",
        f'  <ul class="chips" aria-label="Stack">{chips(stack)}</ul>',
        "</article>",
    ]


def _job(job: dict) -> list[str]:
    return [
        '<li class="reveal">',
        '  <div class="tl-head">',
        f"    <h3>{escape(job['role'])}</h3>",
        f'    <span class="when">{escape(job["dates"])}</span>',
        "  </div>",
        f'  <p class="org">{escape(job["company"])}</p>',
        "  <ul>",
        *(f"    <li>{escape(b)}.</li>" for b in job["resume"]),
        "  </ul>",
        "</li>",
    ]


def _creds() -> list[str]:
    """Credential cards: (label, title, html body)."""
    ed, pub = c.EDUCATION, c.PUBLICATION
    cards = [
        ("Education", ed["degree"], escape(f"{ed['school']}, {ed['dates']}. {ed['detail'].replace(' · ', '. ')}.")),
        ("Publication", f"{pub['short_venue']} (IEEE)",
         f'{escape(pub["title"])}. <a href="{escape(pub["doi_url"])}" rel="noopener">IEEE Xplore</a>'),
    ]
    out = []
    for label, title, body in cards:
        out += [
            '<div class="cred reveal">',
            f'  <p class="cred-label">{escape(label)}</p>',
            f'  <p class="cred-title">{escape(title)}</p>',
            f"  <p>{body}</p>",
            "</div>",
        ]
    return out


def _cert_note() -> str:
    """Certifications folded into one line under the credential cards."""
    certs = "; ".join(f"{name}, {issuer}, {when}" for name, issuer, when in c.CERTIFICATIONS)
    return f'<p class="cred-note reveal"><span class="cred-label">Certification</span>{escape(certs)}</p>'


def _jsonld() -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": c.NAME,
        "jobTitle": c.TITLE,
        "email": f"mailto:{c.EMAIL}",
        "url": c.LINKEDIN[1],
        "sameAs": [url for _, url in c.LINKS],
        "address": {"@type": "PostalAddress", "addressCountry": "PH"},
        "alumniOf": c.EDUCATION["school"],
        "worksFor": {"@type": "Organization", "name": c.EXPERIENCE[0]["company"]},
    }
    text = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return indent(text.splitlines(), 2)


def render(documents_href: str) -> str:
    s = c.SITE
    first, *_, last = c.NAME.split()
    short_name = f"{first} {last}"
    work = [line for w in s["work"] for line in _work_card(w)]
    skills = [
        f'<div class="skill-row reveal"><h3>{escape(label)}</h3><ul class="chips">{chips(items)}</ul></div>'
        for label, items in s["skills"]
    ]
    return Template(TEMPLATE.read_text(encoding="utf-8")).substitute(
        name=escape(c.NAME),
        short_name=escape(short_name),
        initials=escape(first[0] + last[0]),
        title=escape(c.TITLE),
        description=escape(s["description"]),
        og_description=escape(s["og_description"]),
        site_url=escape(s["url"]),
        jsonld=_jsonld(),
        status=escape(s["status"]),
        lead=fmt(s["lead"]),
        email=escape(c.EMAIL),
        linkedin_url=escape(c.LINKEDIN[1]),
        github_url=escape(c.GITHUB[1]),
        resume_pdf=f"{documents_href}/{c.RESUME_STEM}.pdf",
        profile_meta=indent([f"<div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>" for k, v in s["profile"]], 12),
        core_stack=chips(s["core_stack"]),
        about_heading=escape(s["about_heading"]),
        about=indent([f"<p>{fmt(p)}</p>" for p in s["about"]], 10),
        work_intro=escape(s["work_intro"]),
        work=indent(work, 10),
        experience=indent([line for job in c.EXPERIENCE for line in _job(job)], 10),
        skills=indent(skills, 10),
        creds=indent(_creds(), 10),
        cert_note=_cert_note(),
        contact_heading=escape(s["contact_heading"]),
        contact=escape(s["contact"]),
        year=dt.date.today().year,
        location=escape(c.LOCATION),
    )


def build(path: Path, documents_href: str) -> Path:
    path.write_text(render(documents_href), encoding="utf-8", newline="\n")
    return path
