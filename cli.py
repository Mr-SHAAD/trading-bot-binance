import argparse
import os
from dotenv import load_dotenv
from bot.client import get_client
from bot.orders import place_market_order, place_limit_order, place_stop_limit_order, print_order_summary
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price
from bot.logging_config import logger

load_dotenv()

def main():
    parser = argparse.ArgumentParser(
        description='Binance Futures Testnet Trading Bot',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--symbol', required=True, help='Trading pair (e.g. BTCUSDT)')
    parser.add_argument('--side', required=True, help='BUY or SELL')
    parser.add_argument('--type', required=True, dest='order_type', help='MARKET, LIMIT or STOP_LIMIT')
    parser.add_argument('--quantity', required=True, help='Order quantity')
    parser.add_argument('--price', required=False, help='Price (required for LIMIT and STOP_LIMIT)')
    parser.add_argument('--stop-price', required=False, dest='stop_price', help='Stop price (required for STOP_LIMIT)')

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)

        price = None
        stop_price = None

        if order_type in ['LIMIT', 'STOP_LIMIT']:
            if not args.price:
                print("Error: --price is required for LIMIT and STOP_LIMIT orders.")
                return
            price = validate_price(args.price)

        if order_type == 'STOP_LIMIT':
            if not args.stop_price:
                print("Error: --stop-price is required for STOP_LIMIT orders.")
                return
            stop_price = validate_price(args.stop_price)

        print(f"\nOrder Request Summary:")
        print(f"  Symbol   : {symbol}")
        print(f"  Side     : {side}")
        print(f"  Type     : {order_type}")
        print(f"  Quantity : {quantity}")
        if price:
            print(f"  Price    : {price}")
        if stop_price:
            print(f"  Stop     : {stop_price}")

        client = get_client()

        if order_type == 'MARKET':
            order = place_market_order(client, symbol, side, quantity)
        elif order_type == 'LIMIT':
            order = place_limit_order(client, symbol, side, quantity, price)
        else:
            order = place_stop_limit_order(client, symbol, side, quantity, price, stop_price)

        print_order_summary(order, order_type)

    except ValueError as e:
        print(f"\nValidation Error: {e}")
        logger.error(f"Validation error: {e}")
    except Exception as e:
        print(f"\nError: {e}")
        logger.error(f"Fatal error: {e}")

if __name__ == '__main__':
    main()
