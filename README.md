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
