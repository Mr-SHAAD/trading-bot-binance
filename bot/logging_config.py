import logging
import os
from datetime import datetime

def setup_logger():
    os.makedirs('logs', exist_ok=True)
    log_filename = f"logs/trading_{datetime.now().strftime('%Y%m%d')}.log"
    
    logger = logging.getLogger('trading_bot')
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()
