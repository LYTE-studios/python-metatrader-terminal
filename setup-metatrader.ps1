# setup-metatrader.ps1

# Set variables
$installPath = "C:\MetaTrader"
$urlMT4 = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt4/mt4oldsetup.exe"
$urlMT5 = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe"

# Create installation directory
New-Item -Path $installPath -ItemType Directory -Force

# Download MetaTrader 4
Invoke-WebRequest -Uri $urlMT4 -OutFile "$installPath\mt4setup.exe"

# Download MetaTrader 5
Invoke-WebRequest -Uri $urlMT5 -OutFile "$installPath\mt5setup.exe"

# Install MetaTrader 4 silently
Start-Process -FilePath "$installPath\mt4setup.exe" -ArgumentList "/silent" -Wait

# Install MetaTrader 5 silently
Start-Process -FilePath "$installPath\mt5setup.exe" -ArgumentList "/silent" -Wait