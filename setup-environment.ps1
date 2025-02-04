# Set the URL for the Python installer (e.g., latest Python 3.10 64-bit)
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe"
$installerPath = "$env:TEMP\python-installer.exe"

# Download the installer
Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $installerPath

Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Upgrade pip
python -m pip install --upgrade pip

# Install pipenv
pip install pipenv