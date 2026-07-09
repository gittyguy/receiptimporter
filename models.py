from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class ReceiptItem:

    date: str
    shop: str
    article: str
    product: str
    qty: float
    unit_price: float
    line_total: float | None = None
    discount: float = 0.0

@dataclass
class ReceiptDocument:

    source_file: Path
    text: str = ""
    shop: str = ""
    purchase_date: str = ""
    items: list[ReceiptItem] = field(default_factory=list)