@echo off

echo =====================================
echo Building ReceiptImporter.exe
echo =====================================

python -m PyInstaller ^
    --clean ^
    --onefile ^
    --name ReceiptImporter ^
    --add-data "Incoming;Incoming" ^
    --add-data "Processed;Processed" ^
    --add-data "Errors;Errors" ^
    --add-data "logs;logs" ^
    main.py

echo.
echo Build finished.
pause