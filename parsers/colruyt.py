"""
Colruyt receipt parser.
"""

import re

from parser import ReceiptParser


# ----------------------------------------------------------------------
# Regular expressions
# ----------------------------------------------------------------------

PRODUCT_PATTERN = r"""
^\s*
(?P<article>\d{4,6})
\s+
(?P<product>.*?)
\s{2,}
(?P<qty>\d+(?:,\d+)?)
\s+
(?P<unit_price>\d+,\d+)
(?:\s+(?P<line_total>\d+,\d+))?
\s*$
"""

DISCOUNT_PATTERN = r"""
^\s*(?:KORTING|Korting)
.*?
(?P<discount>-\d+,\d+)
\s*$
"""

END_PATTERN = r"""
^(TE\s+BETALEN|BANCONTACT|BETAALD)
"""


class ColruytParser(ReceiptParser):

    shop = "COLRUYT"

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