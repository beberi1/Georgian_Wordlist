<# :
@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "tempScript=%temp%\WordlistGen_%random%.ps1"
copy /y "%~f0" "%tempScript%" >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%tempScript%"
del "%tempScript%"
pause
exit /b
#>

# --- PowerShell ლოგიკა ---

$baseDir = $env:SCRIPT_DIR
if (-not $baseDir.EndsWith("\")) { $baseDir += "\" }

$namesInput = "${baseDir}Names\Names.txt"
$namesUnique = "${baseDir}Names\Unique_Names.txt"
$surnamesInput = "${baseDir}Surnames\Surnames.txt"
$surnamesUnique = "${baseDir}Surnames\Unique_Surnames.txt"

$combFile = "${baseDir}combinations.txt"
$combFile1 = "${baseDir}combinations1.txt"
$filteredComb = "${baseDir}filtered_combinations.txt"
$filteredComb1 = "${baseDir}filtered_combinations1.txt"
$finalOutput = "${baseDir}FullWordlist.txt"

# --- ფუნქციები ---

function Write-ListToFile ($path, $list) {
    [System.IO.File]::WriteAllLines($path, $list, [System.Text.Encoding]::UTF8)
}

function Remove-Duplicates ($inputFile, $outputFile) {
    if (-not (Test-Path $inputFile)) { return }
    Write-Host "   Removing duplicates from: $(Split-Path $inputFile -Leaf)" -ForegroundColor Cyan
    $lines = [System.IO.File]::ReadAllLines($inputFile)
    
    # ვიყენებთ Ordinal-ს ზუსტი შედარებისთვის, რათა 'giorgi' და 'Giorgi' ორივე დარჩეს
    $unique = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
    
    foreach ($line in $lines) { 
        $null = $unique.Add($line.Trim()) 
    }
    Write-ListToFile $outputFile $unique
}

function Upper-Lower-Case ($inputFile, $outputFile) {
    if (-not (Test-Path $inputFile)) { return }
    Write-Host "   Formatting Case (Block style)..." -ForegroundColor Cyan
    $lines = [System.IO.File]::ReadAllLines($inputFile)
    $result = [System.Collections.Generic.List[string]]::new()
    $textInfo = (Get-Culture).TextInfo
    
    # 1. ჯერ ყველა პატარა ასოებით (Python-ის მსგავსად)
    foreach ($line in $lines) { $result.Add($line.ToLower()) }
    
    # 2. შემდეგ ყველა პირველასო დიდით
    foreach ($line in $lines) { $result.Add($textInfo.ToTitleCase($line.ToLower())) }
    
    # 3. ბოლოს ყველა დიდი ასოებით (CAPS)
    foreach ($line in $lines) { $result.Add($line.ToUpper()) }
    
    Write-ListToFile $outputFile $result
}

function Process-Words ($inputFile, $outputFile, $letter, $symbol) {
    Write-Host "   Replacing '$letter' with '$symbol'..." -ForegroundColor Cyan
    
    # ვკითხულობთ არსებულ ხაზებს
    $lines = [System.IO.File]::ReadAllLines($inputFile)
    
    # ვხსნით ფაილს ჩამატების (Append) რეჟიმში ($true), რათა ორიგინალები არ დაიკარგოს
    $writer = [System.IO.StreamWriter]::new($outputFile, $true, [System.Text.Encoding]::UTF8)
    
    foreach ($word in $lines) {
        $word = $word.Trim()
        if ($word.Length -eq 0) { continue }
        
        # 1. First Occurrence (პირველი სიმბოლოს შეცვლა)
        $idx = $word.IndexOf($letter)
        if ($idx -ge 0) {
            $rep1 = $word.Remove($idx, 1).Insert($idx, $symbol)
            $writer.WriteLine($rep1)
        }
        # ELSE ბლოკი ამოვიღე: თუ ასო არ არის, ორიგინალს აღარ ვწერთ, რადგან ისედაც წერია ფაილში.

        # 2. Second Occurrence (მეორე სიმბოლოს შეცვლა)
        $firstIdx = $word.IndexOf($letter)
        if ($firstIdx -ge 0) {
            $secondIdx = $word.IndexOf($letter, $firstIdx + 1)
            if ($secondIdx -ge 0) {
                $rep2 = $word.Remove($secondIdx, 1).Insert($secondIdx, $symbol)
                $writer.WriteLine($rep2)
            }
        }

        # 3. All Occurrences (ყველა სიმბოლოს შეცვლა)
        if ($word.Contains($letter)) {
            $repAll = $word.Replace($letter, $symbol)
            # ვწერთ მხოლოდ იმ შემთხვევაში, თუ ეს ვარიანტი უკვე არ დაგვიწერია პირველ ბიჯზე
            # (თუმცა ზუსტად Python-ის ლოგიკა რომ იყოს, უბრალოდ ვწერთ):
            $writer.WriteLine($repAll)
        }
    }
    $writer.Close()
    $writer.Dispose()
}

function Generate-Combinations ($file1, $file2, $outFile) {
    Write-Host "   Generating Combinations ($file1 + $file2)..." -ForegroundColor Yellow
    if (-not (Test-Path $file1) -or -not (Test-Path $file2)) { return }

    $list1 = [System.IO.File]::ReadAllLines($file1)
    $list2 = [System.IO.File]::ReadAllLines($file2)
    
    $writer = [System.IO.StreamWriter]::new($outFile, $false, [System.Text.Encoding]::UTF8)
    
    $total = $list1.Count
    $current = 0

    foreach ($n in $list1) {
        $n = $n.Trim()
        if ($n.Length -eq 0) { continue }
        $n0 = $n.Substring(0,1)

        foreach ($s in $list2) {
            $s = $s.Trim()
            if ($s.Length -eq 0) { continue }

            $writer.WriteLine("$n$s")
            $writer.WriteLine("${n}_$s")
            $writer.WriteLine("$n-$s")
            $writer.WriteLine("$n.$s")
            $writer.WriteLine("$n/$s")
            $writer.WriteLine("$n\$s")
            $writer.WriteLine("$n0.$s")
            $writer.WriteLine("${n0}_$s")
            $writer.WriteLine("$n0-$s")
            $writer.WriteLine("$n0/$s")
            $writer.WriteLine("$n0\$s")
            $writer.WriteLine("${n0}_$s")
            $writer.WriteLine("$n0$s")
            $writer.WriteLine("${n}da${s}")
        }
        
        $current++
        if ($current % 100 -eq 0) {
            Write-Progress -Activity "Generating Combinations" -Status "Processing Names" -PercentComplete (($current / $total) * 100)
        }
    }
    $writer.Close()
    $writer.Dispose()
}

function Remove-Short-Words ($inFile, $outFile, $minLen) {
    Write-Host "   Filtering short words (<$minLen)..." -ForegroundColor Cyan
    if (-not (Test-Path $inFile)) { return }
    
    $lines = [System.IO.File]::ReadLines($inFile)
    $writer = [System.IO.StreamWriter]::new($outFile, $false, [System.Text.Encoding]::UTF8)
    foreach ($line in $lines) {
        if ($line.Trim().Length -ge $minLen) {
            $writer.WriteLine($line)
        }
    }
    $writer.Close()
    $writer.Dispose()
}

# --- ძირითადი შესრულება ---

Clear-Host
Write-Host "DAIWYEBULIA WORDLIST GENERACIA..." -ForegroundColor Green

# 1. მომზადება (სუფთა სიტყვების დაგენერირება)
Remove-Duplicates $surnamesInput $surnamesUnique
Remove-Duplicates $namesInput $namesUnique
Upper-Lower-Case $surnamesUnique $surnamesUnique
Upper-Lower-Case $namesUnique $namesUnique

# 2. სიმბოლოების ჩანაცვლება (Append რეჟიმში - ორიგინალებს არ შლის)
Process-Words $namesUnique $namesUnique "i" "!"
Process-Words $namesUnique $namesUnique "e" "3"
Process-Words $namesUnique $namesUnique "o" "0"

Process-Words $surnamesUnique $surnamesUnique "i" "!"
Process-Words $surnamesUnique $surnamesUnique "e" "3"
Process-Words $surnamesUnique $surnamesUnique "o" "0"

# მეორედ გაცხრილვა (ახლა უკვე Case Sensitive)
Remove-Duplicates $surnamesUnique $surnamesUnique
Remove-Duplicates $namesUnique $namesUnique

# 3. კომბინაციები
Generate-Combinations $namesUnique $surnamesUnique $combFile
Generate-Combinations $surnamesUnique $namesUnique $combFile1

# 4. ფილტრაცია
Remove-Short-Words $combFile $filteredComb 8
Remove-Short-Words $combFile1 $filteredComb1 8

# 5. გაერთიანება
Write-Host "   Merging files to FullWordlist.txt..." -ForegroundColor Green

$destStream = [System.IO.File]::Create($finalOutput)
foreach ($filePath in @($filteredComb, $filteredComb1)) {
    if (Test-Path $filePath) {
        $srcStream = [System.IO.File]::OpenRead($filePath)
        $srcStream.CopyTo($destStream)
        $srcStream.Close()
        $srcStream.Dispose()
    }
}
$destStream.Close()
$destStream.Dispose()

# 6. გასუფთავება
Write-Host "   Cleaning temp files..." -ForegroundColor Gray
Remove-Item $namesUnique -ErrorAction SilentlyContinue
Remove-Item $surnamesUnique -ErrorAction SilentlyContinue
Remove-Item $combFile -ErrorAction SilentlyContinue
Remove-Item $combFile1 -ErrorAction SilentlyContinue
Remove-Item $filteredComb -ErrorAction SilentlyContinue
Remove-Item $filteredComb1 -ErrorAction SilentlyContinue

Write-Host "`n[V] Yvelaferi dasrulda warmatebit!" -ForegroundColor Green
Write-Host "Shedegi: $finalOutput`n" -ForegroundColor White