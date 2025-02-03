# start-metatrader.ps1

# Define the installation directories and executable paths
$mt4Path = "C:\MetaTrader\MT4\terminal.exe" # Adjust the path based on your actual install location
$mt5Path = "C:\MetaTrader\MT5\terminal64.exe" # Adjust the path based on your actual install location

# Function to start MetaTrader terminal
Function Start-MetaTrader($path) {
    if (Test-Path $path) {
        Start-Process -FilePath $path
        Write-Host "Started MetaTrader terminal: $path"
    } else {
        Write-Host "MetaTrader terminal not found at: $path"
    }
}

# Start each MetaTrader terminal
Start-MetaTrader $mt4Path
Start-MetaTrader $mt5Path
