import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # 数据库配置
    DB_USER = os.getenv('DB_USER', 'crypto')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'crypto123')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'crypto_trades')
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    # Binance配置
    BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
    BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')
    BINANCE_SYMBOLS = os.getenv('BINANCE_SYMBOLS', '').split(',')
    BINANCE_ENABLED = os.getenv('BINANCE_ENABLED', 'true').lower() == 'true'
    
    # OKX配置
    OKX_API_KEY = os.getenv('OKX_API_KEY')
    OKX_API_SECRET = os.getenv('OKX_API_SECRET')
    OKX_PASSPHRASE = os.getenv('OKX_PASSPHRASE')
    OKX_SYMBOLS = os.getenv('OKX_SYMBOLS', '').split(',')
    OKX_ENABLED = os.getenv('OKX_ENABLED', 'true').lower() == 'true'
    
    # 全局配置
    UPDATE_INTERVAL = int(os.getenv('UPDATE_INTERVAL', 60)) 