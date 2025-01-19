import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # PostgreSQL connection URI
    DB_USER = os.getenv('DB_USER', 'crypto')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'crypto123')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'crypto_trades')
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    # 交易所配置
    EXCHANGES = {
        'binance': {
            'api_key': os.getenv('BINANCE_API_KEY'),
            'api_secret': os.getenv('BINANCE_API_SECRET'),
            'symbols': os.getenv('BINANCE_SYMBOLS', 'BTCUSDT,ETHUSDT').split(','),
            'enabled': os.getenv('BINANCE_ENABLED', 'true').lower() == 'true'
        }
        # 可以添加其他交易所配置
        # 'huobi': {
        #     'api_key': os.getenv('HUOBI_API_KEY'),
        #     'api_secret': os.getenv('HUOBI_API_SECRET'),
        #     'symbols': os.getenv('HUOBI_SYMBOLS', 'btcusdt,ethusdt').split(','),
        #     'enabled': os.getenv('HUOBI_ENABLED', 'false').lower() == 'true'
        # }
    }
    
    # 全局配置
    UPDATE_INTERVAL = int(os.getenv('UPDATE_INTERVAL', '60'))  # 更新间隔（秒） 