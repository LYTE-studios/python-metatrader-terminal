# start-metatrader.ps1

# Define the installation directories and executable paths
$mt4Executable = "C:\MetaTrader\MT4\terminal.exe" # Adjust according to actual installation
$mt5Executable = "C:\MetaTrader\MT5\terminal64.exe" # Adjust according to actual installation

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
