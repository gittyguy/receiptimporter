"""
Logging configuration.
"""

import logging

from config import LOG_FOLDER, LOG_FILE


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.
    """

    LOG_FOLDER.mkdir(exist_ok=True)

    logger = logging.getLogger("ReceiptImporter")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)-8s %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger