"""
Application configuration.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Folder configuration
# ------------------------------------------------------------------

BASE_FOLDER = Path(__file__).resolve().parent

INCOMING_FOLDER = BASE_FOLDER / "Incoming"
PROCESSED_FOLDER = BASE_FOLDER / "Processed"
ERROR_FOLDER = BASE_FOLDER / "Errors"
LOG_FOLDER = BASE_FOLDER / "logs"

EXCEL_FILE = BASE_FOLDER / "Expenses.xlsx"

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------

LOG_FILE = LOG_FOLDER / "receipt_importer.log"

# ------------------------------------------------------------------
# Supported input files
# ------------------------------------------------------------------

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".txt",
}