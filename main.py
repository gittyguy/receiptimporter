"""
Receipt Importer

Main application.
"""

from pathlib import Path
import shutil
import traceback

from config import ERROR_FOLDER
from config import EXCEL_FILE
from config import INCOMING_FOLDER
from config import PROCESSED_FOLDER

from detect import get_parser

from excel_writer import ExcelWriter

from file_processor import (
    load_receipt,
    save_extracted)