<# :
@echo off
setlocal

:: ვიგებთ მიმდინარე საქაღალდის მისამართს (%~dp0) და ვინახავთ ცვლადში
set "SCRIPT_DIR=%~dp0"

:: ვქმნით დროებით ასლს Temp-ში
set "tempScript=%temp%\GenerateNumbers_%random%.ps1"
copy /y "%~f0" "%tempScript%" >nul

:: ვუშვებთ PowerShell-ს (ის დაინახავს SCRIPT_DIR ცვლადს)
powershell -NoProfile -ExecutionPolicy Bypass -File "%tempScript%"

:: ვშლით დროებით ფაილს
del "%tempScript%"
pause
exit /b
#>

# --- აქედან იწყება PowerShell კოდი ---

$prefixes = @(501, 504, 505, 510, 511, 522, 533, 500, 544, 550, 555, 568, 569, 571, 574, 575, 579, 585, 591, 592, 595, 596, 597, 598, 599, 551)

# ვიღებთ Batch-იდან გადმოცემულ მისამართს
$targetDir = $env:SCRIPT_DIR

# ვქმნით სრული ფაილის მისამართს
$outputFile = Join-Path -Path $targetDir -ChildPath "numbers.txt"

Clear-Host
Write-Host "`n   NOMREBIS GENERACIA..." -ForegroundColor Cyan
Write-Host "   ---------------------" -ForegroundColor DarkGray
Write-Host "   Location: $outputFile" -ForegroundColor Yellow

# სწრაფი ჩამწერი
$writer = [System.IO.StreamWriter]::new($outputFile)

$total = $prefixes.Count
$current = 0

foreach ($prefix in $prefixes) {
    $current++
    
    $percent = [math]::Round(($current / $total) * 100)
    Write-Progress -Activity "Generacia..." -Status "Mushavdeba indeksi: $prefix ($current / $total)" -PercentComplete $percent

    $prefixStr = [string]$prefix
    $digitsNeeded = 9 - $prefixStr.Length
    $maxNum = [math]::Pow(10, $digitsNeeded)
    
    $formatString = "D" + $digitsNeeded

    for ($i = 0; $i -lt $maxNum; $i++) {
        $line = $prefixStr + $i.ToString($formatString)
        $writer.WriteLine($line)
    }
}

$writer.Close()
$writer.Dispose()

Write-Host "`n   [V] DASRULDA WARMATEBIT!" -ForegroundColor Green
Write-Host "   Faili shenaxulia aq: $outputFile`n" -ForegroundColor Gray