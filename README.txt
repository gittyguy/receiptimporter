# Receipt Importer

Automatically imports supermarket receipts into Excel.

Currently supported supermarkets

- SPAR
- OKAY
- Colruyt

---

## Folder structure

```
ReceiptImporter/

Incoming/
Processed/
Errors/
logs/

Expenses.xlsx

ReceiptImporter.exe
```
Final folder structure
ReceiptImporter/

config.py
detect.py
excel_writer.py
file_processor.py
logger.py
main.py
models.py
parser.py
pdf_to_text.py

requirements.txt

build.bat
build.ps1

README.md

Incoming/
Processed/
Errors/
logs/

parsers/

    __init__.py
    spar.py
    okay.py
    colruyt.py
---

## Usage

Copy one or more receipts into

```
Incoming
```

Supported files

```
PDF
TXT
```

Run

```
ReceiptImporter.exe
```

The application will

1. Detect the supermarket.
2. Convert PDF files to text.
3. Parse all purchased products.
4. Append the products to Excel.
5. Move processed files to Processed.
6. Save extracted text beside processed PDFs.
7. Move invalid receipts to Errors.

Incoming will be empty after processing.

---

## Excel

Columns

| Purchase Date | Product | Total Price | Shop |

The Total Price column contains an Excel formula.

Example

```
=3.49-0.70
```

or

```
=9.00
```

---

## Building

Install Python 3.12 or newer.

Install dependencies

```
pip install -r requirements.txt
```

Build

```
build.bat
```

The executable is generated in

```
dist/
```

Copy

```
ReceiptImporter.exe
```

to the destination computer.

Python is not required on the destination computer.

---

## Adding a supermarket

Create a new parser inside

```
parsers/
```

The parser only needs

- PRODUCT_PATTERN
- DISCOUNT_PATTERN
- END_PATTERN

and to inherit from

```
ReceiptParser
```

Finally register it in

```
detect.py
```

No other files need to be modified.