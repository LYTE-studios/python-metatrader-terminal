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

# Install and move MetaTrader 4
Start-Process -FilePath "$tempDir\mt4setup.exe" -ArgumentList "/silent" -Wait

# Install and move MetaTrader 5
Start-Process -FilePath "$tempDir\mt5setup.exe" -ArgumentList "/silent" -Wait