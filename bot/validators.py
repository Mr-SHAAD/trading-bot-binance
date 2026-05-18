VALID_SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'XRPUSDT']
VALID_SIDES = ['BUY', 'SELL']
VALID_ORDER_TYPES = ['MARKET', 'LIMIT', 'STOP_LIMIT']

def validate_symbol(symbol: str) -> str:
    symbol = symbol.upper()
    if symbol not in VALID_SYMBOLS:
        raise ValueError(f"Invalid symbol '{symbol}'. Valid: {', '.join(VALID_SYMBOLS)}")
    return symbol

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in VALID_SIDES:
        raise ValueError(f"Invalid side '{side}'. Must be BUY or SELL.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type '{order_type}'. Must be MARKET, LIMIT or STOP_LIMIT.")
    return order_type

def validate_quantity(quantity: str) -> float:
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0.")
        return qty
    except (TypeError, ValueError):
        raise ValueError(f"Invalid quantity '{quantity}'. Must be a positive number.")

def validate_price(price: str) -> float:
    try:
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be greater than 0.")
        return p
    except (TypeError, ValueError):
        raise ValueError(f"Invalid price '{price}'. Must be a positive number.")
