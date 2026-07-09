Write-Host ""
Write-Host "Building ReceiptImporter.exe"
Write-Host ""

python -m PyInstaller `
    --clean `
    --onefile `
    --name ReceiptImporter `
    --add-data "Incoming;Incoming" `
    --add-data "Processed;Processed" `
    --add-data "Errors;Errors" `
    --add-data "logs;logs" `
    main.py

Write-Host ""
Write-Host "Finished."