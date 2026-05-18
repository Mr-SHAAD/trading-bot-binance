import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import logger

def get_client() -> Client:
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    if not api_key or not api_secret:
        raise ValueError("API keys not found. Check your .env file.")
    
    client = Client(api_key, api_secret, testnet=True)
    client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
    logger.info("Binance Futures Testnet client initialized")
    return client
