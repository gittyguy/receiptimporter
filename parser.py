"""
Generic receipt parser.
"""

from __future__ import annotations
import re
from abc import ABC
from models import ReceiptDocument
from models import ReceiptItem

DATE_PATTERN = re.compile(r"(?P<date>\d{2}/\d{2}/\d{4})\s+\d{2}:\d{2}")

class ReceiptParser(ABC):

    shop = ""
    product_pattern = None
    discount_pattern = None
    end_pattern = None

    def parse(self,receipt: ReceiptDocument,) -> None:
        receipt.shop = self.shop
        self._extract_purchase_date(receipt)
        for line in receipt.text.splitlines():
            if self.end_pattern.match(line):
                break
            product = self.product_pattern.match(line)
            if product:
                qty = float(product.group("qty").replace(",", "."))
                unit_price = float(product.group("unit_price").replace(",", "."))
                line_total = product.groupdict().get("line_total")
                if line_total:
                    line_total = float(line_total.replace(",", "."))
                receipt.items.append(
                    ReceiptItem(
                        date=receipt.purchase_date,
                        shop=self.shop,
                        article=product.group("article"),
                        product=product.group("product").strip(),
                        qty=qty,
                        unit_price=unit_price,
                        line_total=line_total,
                        discount=0.0,
                    ))
                continue
            discount = self.discount_pattern.match(line)
            if discount and receipt.items:
                receipt.items[-1].discount = abs(
                    float(discount.group("discount").replace(",", ".")))

    def _extract_purchase_date(self,receipt: ReceiptDocument,) -> None:
        match = DATE_PATTERN.search(receipt.text)
        if match:
            receipt.purchase_date = match.group("date")