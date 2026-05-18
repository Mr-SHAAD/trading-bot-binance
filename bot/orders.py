from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import logger

def place_market_order(client: Client, symbol: str, side: str, quantity: float) -> dict:
    logger.info(f"Placing MARKET order | {side} {quantity} {symbol}")
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"MARKET order placed successfully | OrderId: {order.get('orderId', 'N/A')}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API error: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise

def place_limit_order(client: Client, symbol: str, side: str, quantity: float, price: float) -> dict:
    logger.info(f"Placing LIMIT order | {side} {quantity} {symbol} @ {price}")
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
        logger.info(f"LIMIT order placed successfully | OrderId: {order.get('orderId', 'N/A')}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API error: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise

def place_stop_limit_order(client: Client, symbol: str, side: str, quantity: float, price: float, stop_price: float) -> dict:
    logger.info(f"Placing STOP_LIMIT order | {side} {quantity} {symbol} @ {price} | Stop: {stop_price}")
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP',
            quantity=quantity,
            price=str(price),
            stopPrice=str(stop_price),
            timeInForce='GTC'
        )
        logger.info(f"STOP_LIMIT order placed successfully | OrderId: {order.get('orderId', 'N/A')}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API error: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise

def print_order_summary(order: dict, order_type: str):
    print("\n" + "="*50)
    print(f"  ORDER PLACED SUCCESSFULLY")
    print("="*50)
    print(f"  Order ID     : {order.get('orderId', 'N/A')}")
    print(f"  Symbol       : {order.get('symbol', 'N/A')}")
    print(f"  Side         : {order.get('side', 'N/A')}")
    print(f"  Type         : {order_type}")
    print(f"  Status       : {order.get('status', 'N/A')}")
    print(f"  Quantity     : {order.get('origQty', 'N/A')}")
    avg = order.get('avgPrice', '0')
    if avg and float(avg) > 0:
        print(f"  Avg Price    : {avg}")
    price = order.get('price', '0')
    if price and float(price) > 0:
        print(f"  Limit Price  : {price}")
    stop = order.get('stopPrice', '0')
    if stop and float(stop) > 0:
        print(f"  Stop Price   : {stop}")
    print(f"  Executed Qty : {order.get('executedQty', '0')}")
    print("="*50 + "\n")
