# Specify target installation directories for post-installation move
$mt4TargetPath = "C:\MetaTrader\MT4"
$mt5TargetPath = "C:\MetaTrader\MT5"

# URLs for setup files
$urlMT4 = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt4/mt4oldsetup.exe"
$urlMT5 = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe"

# Download installers to a temporary directory
$tempDir = "$env:TEMP\MetaTraderSetups"

if (-Not (Test-Path -Path $tempDir)) {
    New-Item -Path $tempDir -ItemType Directory -Force
}

Invoke-WebRequest -Uri $urlMT4 -OutFile "$tempDir\mt4setup.exe"
Invoke-WebRequest -Uri $urlMT5 -OutFile "$tempDir\mt5setup.exe"

# Default installation directories (modify according to observed paths post-installation)
$defaultMt4Path = "C:\Program Files (x86)\MetaTrader 4"
$defaultMt5Path = "C:\Program Files\MetaTrader 5"

# Function to move installations
function Move-Installation {
    param (
        [string]$sourcePath,
        [string]$destinationPath
    )
    if (Test-Path $sourcePath) {
        Move-Item -Path $sourcePath -Destination $destinationPath -Force -Recurse
        Write-Host "Moved $sourcePath to $destinationPath"
    } else {
        Write-Host "Source path $sourcePath not found"
    }
}

# Install and move MetaTrader 4
Start-Process -FilePath "$tempDir\mt4setup.exe" -ArgumentList "/silent" -Wait
Move-Installation -sourcePath $defaultMt4Path -destinationPath $mt4TargetPath

# Install and move MetaTrader 5
Start-Process -FilePath "$tempDir\mt5setup.exe" -ArgumentList "/silent" -Wait
Move-Installation -sourcePath $defaultMt5Path -destinationPath $mt5TargetPath
