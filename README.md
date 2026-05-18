# Trading Bot – Binance Futures Testnet (USDT-M)

A simplified Python CLI trading bot that places orders on Binance Futures Testnet.

## Features

- Place **Market** and **Limit** orders (BUY/SELL)
- Bonus: **Stop-Limit** order support
- CLI input via `argparse`
- Input validation with clear error messages
- Structured logging to file and console
- Clean separation: client layer, order layer, validation layer, CLI layer

## Project Structure

\`\`\`
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance Futures Testnet client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logger setup
├── logs/                  # Auto-created log files
├── cli.py                 # CLI entry point
├── requirements.txt
├── .env.example
└── README.md
\`\`\`

## Setup Instructions

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/trading_bot.git
cd trading_bot
\`\`\`

### 2. Install dependencies
\`\`\`bash
pip3 install -r requirements.txt
\`\`\`

### 3. Configure API keys
\`\`\`bash
cp .env.example .env
\`\`\`
Open .env and add your Binance Futures Testnet API credentials:
\`\`\`
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
\`\`\`
Get your testnet API keys from: https://testnet.binancefuture.com

## How to Run

### Market Order
\`\`\`bash
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
python3 cli.py --symbol ETHUSDT --side SELL --type MARKET --quantity 0.01
\`\`\`

### Limit Order
\`\`\`bash
python3 cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 75000
\`\`\`

### Stop-Limit Order (Bonus)
\`\`\`bash
python3 cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 80000 --stop-price 79000
\`\`\`

## CLI Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| --symbol | Yes | Trading pair (BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT) |
| --side | Yes | BUY or SELL |
| --type | Yes | MARKET, LIMIT, or STOP_LIMIT |
| --quantity | Yes | Order quantity (positive number) |
| --price | For LIMIT/STOP_LIMIT | Limit price |
| --stop-price | For STOP_LIMIT | Stop trigger price |

## Sample Output

\`\`\`
Order Request Summary:
  Symbol   : BTCUSDT
  Side     : BUY
  Type     : MARKET
  Quantity : 0.001

==================================================
  ORDER PLACED SUCCESSFULLY
==================================================
  Order ID     : 13157551174
  Symbol       : BTCUSDT
  Side         : BUY
  Type         : MARKET
  Status       : NEW
  Quantity     : 0.0010
  Executed Qty : 0.0000
==================================================
\`\`\`

## Logging

All API requests, responses, and errors are logged to:
- **Console** — real-time output
- **File** — logs/trading_YYYYMMDD.log

Log format:
\`\`\`
2026-05-19 00:13:45,525 | INFO | Placing MARKET order | BUY 0.001 BTCUSDT
2026-05-19 00:13:45,815 | INFO | MARKET order placed successfully | OrderId: 13157551174
\`\`\`

## Assumptions

- Only USDT-M Futures Testnet is supported
- Supported symbols: BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT
- For Stop-Limit BUY: stop price must be above current market price
- For Stop-Limit SELL: stop price must be below current market price
- timeInForce is GTC for Limit orders
- Testnet base URL: https://testnet.binancefuture.com

## Requirements

- Python 3.x
- Binance Futures Testnet account with API credentials
