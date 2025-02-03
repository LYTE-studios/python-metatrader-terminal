# Python MetaTrader Terminal

## Overview

This project aims to create a Python-based web server that interfaces with MetaTrader 4 and MetaTrader 5 trading terminals. The server will provide a REST API for placing trades and fetching trade data, leveraging Docker to run MetaTrader terminals in isolated environments.

## Features

- Authenticate and manage MT4/MT5 trading accounts.
- Place trades and fetch trade data via a REST API.
- Distribute tasks across multiple MetaTrader terminals for concurrent processing.
- Fully containerized using Docker for easy deployment and scalability.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.8+ and Django installed for development.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-metatrader-terminal.git
   cd python-metatrader-terminal
   ```

### Usage

**Starting MetaTrader Terminals**

To start the MetaTrader terminals without reinstalling them, use the `start-metatrader.ps1` script. This script is designed to launch MetaTrader 4 and MetaTrader 5 from their installed locations.

1. **Open PowerShell as Administrator**:
   - Ensure you have administrative privileges to run the script.

2. **Navigate to the directory containing the script**:
   - Use `cd` to change to the directory where `start-metatrader.ps1` is located.

3. **Run the following command to execute the script**:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force
   .\start-metatrader.ps1
   ```

This command will launch the MetaTrader terminals if they are installed at the specified paths in the script.

## Future Enhancements

1. Implement logging and monitoring for the API and terminals.
2. Add support for additional trading platforms if needed.
3. Optimize performance and scalability.
```

This updated section should display correctly and convey the instructions effectively. Ensure your markdown viewer or editor supports standard markdown rendering. Adjust paths and repository details as necessary for your specific use case.