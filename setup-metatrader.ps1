# setup-metatrader.ps1

# Set variables
$baseInstallPath = "C:\MetaTrader"
$urlMT4 = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt4/mt4oldsetup.exe"
$urlMT5 = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe"

# Download installers to temporary directory
$tempDir = "$env:TEMP\MetaTraderSetups"
New-Item -Path $tempDir -ItemType Directory -Force
Invoke-WebRequest -Uri $urlMT4 -OutFile "$tempDir\mt4setup.exe"
Invoke-WebRequest -Uri $urlMT5 -OutFile "$tempDir\mt5setup.exe"

# Attempt installation with specified path (if possible)
function Install-MetaTrader {
    param (
        [string]$installerPath,
        [string]$targetInstallPath
    )

    # Check if a custom path can be set via arguments
    Start-Process -FilePath $installerPath -ArgumentList "/silent", "/DIR=$targetInstallPath" -Wait
}

Install-MetaTrader -installerPath "$tempDir\mt4setup.exe" -targetInstallPath "$baseInstallPath\MT4"
Install-MetaTrader -installerPath "$tempDir\mt5setup.exe" -targetInstallPath "$baseInstallPath\MT5"
