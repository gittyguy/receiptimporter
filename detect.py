"""
Detect which supermarket parser should be used.
"""

from parsers.colruyt import ColruytParser
from parsers.okay import OkayParser
from parsers.spar import SparParser


def get_parser(text: str):
    """
    Return the correct parser for the supplied receipt.
    """

    upper = text.upper()

    if "SPAR" in upper:
        return SparParser()

    if "OKAY" in upper:
        return OkayParser()

    if "COLRUYT" in upper:
        return ColruytParser()

    raise ValueError(
        "Unknown supermarket."
    )