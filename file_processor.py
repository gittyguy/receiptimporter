"""
Loads receipt files.

Supported formats

    *.pdf
    *.txt
"""

from pathlib import Path

from config import SUPPORTED_EXTENSIONS
from models import ReceiptDocument
from pdf_to_text import pdf_to_text


def load_receipt(path: Path) -> ReceiptDocument:
    """
    Load one receipt.
    """

    extension = path.suffix.lower()
    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type {extension}")
    receipt = ReceiptDocument(source_file=path)
    if extension == ".pdf":
        receipt.text = pdf_to_text(path)
    else:
        receipt.text = path.read_text(encoding="utf-8",errors="ignore",)
    return receipt

def save_extracted_text(receipt: ReceiptDocument,destination: Path,) -> None:
    """
    Save extracted receipt text.
    """

    txt_file = destination / (receipt.source_file.stem + ".txt")
    txt_file.write_text(receipt.text,encoding="utf-8",)