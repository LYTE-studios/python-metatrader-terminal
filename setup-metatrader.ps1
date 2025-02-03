# setup-metatrader.ps1

# Set base installation path
$baseInstallPath = "C:\MetaTrader"

# Set up directories for each version
$mt4Path = "$baseInstallPath\MT4"
$mt5Path = "$baseInstallPath\MT5"

# URLs for setup files
$urlMT4 = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt4/mt4oldsetup.exe"
$urlMT5 = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe"

# Create installation directories
New-Item -Path $mt4Path -ItemType Directory -Force
New-Item -Path $mt5Path -ItemType Directory -Force

# Download MetaTrader 4
Invoke-WebRequest -Uri $urlMT4 -OutFile "$mt4Path\mt4setup.exe"

# Download MetaTrader 5
Invoke-WebRequest -Uri $urlMT5 -OutFile "$mt5Path\mt5setup.exe"

# Install MetaTrader 4 silently
Start-Process -FilePath "$mt4Path\mt4setup.exe" -ArgumentList "/silent" -Wait

# Install MetaTrader 5 silently
Start-Process -FilePath "$mt5Path\mt5setup.exe" -ArgumentList "/silent" -Wait
