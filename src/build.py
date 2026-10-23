"""Build the portfolio site and the resume/CV from src/content.py.

Outputs (paths relative to the repo root)
  index.html                                     website (GitHub Pages root)
  documents/Lorenzo_Ocampo_Resume_2026.md|docx|pdf
  documents/Lorenzo_Ocampo_CV_2026.md|docx|pdf

Usage:  python src/build.py [--no-pdf]
Requires: python-docx; docx2pdf + Microsoft Word for the PDF step.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import documents
import webpage

ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS = "documents"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-pdf", action="store_true", help="skip the Word-based PDF export")
    args = ap.parse_args()

    for path in documents.build(ROOT / DOCUMENTS, pdf=not args.no_pdf):
        print("built", path.relative_to(ROOT))
    print("built", webpage.build(ROOT / "index.html", DOCUMENTS).relative_to(ROOT))


if __name__ == "__main__":
    main()
