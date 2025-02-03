# start-metatrader.ps1

$defaultMt4Path = "C:\Program Files (x86)\MetaTrader 4"
$defaultMt5Path = "C:\Program Files\MetaTrader 5"

# Define the installation directories and executable paths
$mt4Executable = "$defaultMt4Path\terminal.exe" # Adjust according to actual installation
$mt5Executable = "$defaultMt5Path\terminal64.exe" # Adjust according to actual installation

# Function to start a MetaTrader terminal
Function Start-MetaTrader($executablePath) {
    if (Test-Path $executablePath) {
        Start-Process -FilePath $executablePath
        Write-Host "Started MetaTrader terminal: $executablePath"
    } else {
        Write-Host "MetaTrader terminal not found at: $executablePath"
    }
}

# Start each MetaTrader terminal
Start-MetaTrader $mt4Executable
Start-MetaTrader $mt5Executable
