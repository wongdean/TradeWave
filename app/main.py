import time
from app.services.binance_service import BinanceService
from app.services.okx_service import OKXService
from config.config import Config
from database import Database
import logging

def main():
    # 设置日志
    logging.basicConfig(level=logging.INFO)
    
    # 初始化数据库
    db = Database()
    
    # 初始化服务
    services = []
    
    # 添加Binance服务
    if Config.BINANCE_ENABLED and Config.BINANCE_API_KEY and Config.BINANCE_API_SECRET:
        binance_service = BinanceService(
            api_key=Config.BINANCE_API_KEY,
            api_secret=Config.BINANCE_API_SECRET
        )
        services.append((binance_service, Config.BINANCE_SYMBOLS))
        
    # 添加OKX服务
    if Config.OKX_ENABLED and Config.OKX_API_KEY and Config.OKX_API_SECRET:
        okx_service = OKXService(
            api_key=Config.OKX_API_KEY,
            api_secret=Config.OKX_API_SECRET,
            passphrase=Config.OKX_PASSPHRASE
        )
        services.append((okx_service, Config.OKX_SYMBOLS))
    
    while True:
        try:
            for service, symbols in services:
                for symbol in symbols:
                    trades = service.get_trades(symbol)
                    if trades:
                        db.save_trades(trades)
                        logging.info(f"Saved {len(trades)} trades for {symbol}")
                    
            time.sleep(Config.UPDATE_INTERVAL)
            
        except Exception as e:
            logging.error(f"Error in main loop: {str(e)}")
            time.sleep(Config.UPDATE_INTERVAL)

if __name__ == "__main__":
    main() 