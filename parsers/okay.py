"""
OKAY receipt parser.
"""

import re

from parser import ReceiptParser


# ----------------------------------------------------------------------
# Regular expressions
# ----------------------------------------------------------------------

PRODUCT_PATTERN = r"""
^\s*
(?P<article>\d{4,5})
\s+
(?P<product>.*?)
\s{2,}
(?P<qty>\d+)
\s+
(?P<unit_price>\d+,\d+)
(?:\s+(?P<line_total>\d+,\d+))?
\s*$
"""

DISCOUNT_PATTERN = r"""
^\s*Okay\s+korting
.*?
(?P<discount>-\d+,\d+)
\s*$
"""

END_PATTERN = r"""
^(Te\s+betalen|BANCONTACT|Totaal\s+betaald)
"""


class OkayParser(ReceiptParser):

    shop = "OKAY"

    product_pattern = re.compile(
        PRODUCT_PATTERN,
        re.VERBOSE,
    )

    discount_pattern = re.compile(
        DISCOUNT_PATTERN,
        re.VERBOSE | re.IGNORECASE,
    )

    end_pattern = re.compile(
        END_PATTERN,
        re.IGNORECASE | re.VERBOSE,
    )