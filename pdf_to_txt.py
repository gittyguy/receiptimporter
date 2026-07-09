"""
Convert a PDF receipt to text.

Priority:
    1. pdfplumber
    2. pdfminer.six
    3. PyMuPDF
"""

from pathlib import Path


def pdf_to_text(filename: Path) -> str:

    # ------------------------------------------------------------------
    # pdfplumber
    # ------------------------------------------------------------------

    try:
        import pdfplumber
        text = []
        with pdfplumber.open(filename) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return "\n".join(text)
    except Exception:
        pass

    # ------------------------------------------------------------------
    # pdfminer
    # ------------------------------------------------------------------

    try:
        from pdfminer.high_level import extract_text
        return extract_text(filename)
    except Exception:
        pass

    # ------------------------------------------------------------------
    # PyMuPDF
    # ------------------------------------------------------------------

    try:
        import fitz
        document = fitz.open(filename)
        text = []
        for page in document:
            text.append(page.get_text())
        document.close()
        return "\n".join(text)
    except Exception:
        pass

    raise RuntimeError(
        "Unable to extract text from PDF."
    )