# 🤖 Binance Futures Testnet Trading Bot

> A clean, production-style Python CLI bot for placing orders on **Binance Futures Testnet (USDT-M)**.
> Built with proper layered architecture, input validation, and structured logging.

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 📈 Order Types | Market, Limit, Stop-Limit (Bonus) |
| 🔄 Sides | BUY and SELL |
| 🖥️ CLI Interface | Clean argparse-based input |
| ✅ Validation | Symbol, side, type, quantity, price checks |
| 📝 Logging | File + console logging with timestamps |
| 🏗️ Architecture | Layered: client → orders → validators → CLI |
| 🔒 Security | API keys via .env (never hardcoded) |

---

## 📁 Project Structure

\`\`\`
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py           # Binance client wrapper
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation
│   └── logging_config.py   # Logger setup
├── logs/
│   └── trading_YYYYMMDD.log
├── cli.py                  # CLI entry point
├── .env.example
├── requirements.txt
└── README.md
\`\`\`

---

## ⚙️ Setup Instructions

### Step 1 — Clone the repository
\`\`\`bash
git clone https://github.com/Mr-SHAAD/trading-bot-binance.git
cd trading-bot-binance
\`\`\`

### Step 2 — Install dependencies
\`\`\`bash
pip3 install -r requirements.txt
\`\`\`

### Step 3 — Configure API keys
\`\`\`bash
cp .env.example .env
\`\`\`

Open .env and add your Binance Futures Testnet credentials:
\`\`\`env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
\`\`\`

> Get your free testnet API keys from: https://testnet.binancefuture.com

---

## 🚀 How to Run

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
python3 cli.py --symbol BTCUSDT --side SELL --type STOP_LIMIT --quantity 0.001 --price 65000 --stop-price 66000
\`\`\`

---

## 🔧 CLI Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| --symbol | Yes | BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT |
| --side | Yes | BUY or SELL |
| --type | Yes | MARKET, LIMIT, or STOP_LIMIT |
| --quantity | Yes | Positive number (e.g. 0.001) |
| --price | LIMIT/STOP_LIMIT | Limit price |
| --stop-price | STOP_LIMIT only | Stop trigger price |

---

## 📤 Sample Output

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

---

## 📋 Logging

Every API request, response, and error is logged automatically.

Log location: logs/trading_YYYYMMDD.log

\`\`\`
2026-05-19 00:13:45,525 | INFO  | Binance Futures Testnet client initialized
2026-05-19 00:13:45,525 | INFO  | Placing MARKET order | BUY 0.001 BTCUSDT
2026-05-19 00:13:45,815 | INFO  | MARKET order placed successfully | OrderId: 13157551174
\`\`\`

---

## 📌 Assumptions

- Only USDT-M Futures Testnet is supported
- Supported symbols: BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT
- Stop-Limit BUY: stop price must be above current market price
- Stop-Limit SELL: stop price must be below current market price
- timeInForce defaults to GTC for Limit orders
- Testnet base URL: https://testnet.binancefuture.com
- Minimum quantity for BTC is 0.001

---

## 📦 Tech Stack

- Python 3.x
- python-binance
- argparse
- python-dotenv
- Python logging module
