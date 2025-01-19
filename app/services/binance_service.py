from datetime import datetime
from binance.client import Client
from config.config import Config
from app.models.trade import Trade, Session

class BinanceService:
    def __init__(self):
        config = Config.EXCHANGES['binance']
        self.client = Client(config['api_key'], config['api_secret'])
        self.symbols = config['symbols']
        
    def get_recent_trades(self):
        """获取最近的交易数据"""
        try:
            session = Session()
            
            for symbol in self.symbols:
                trades = self.client.get_recent_trades(symbol=symbol, limit=1000)
                
                for trade in trades:
                    # 创建新的交易记录
                    new_trade = Trade(
                        exchange='binance',
                        symbol=symbol,
                        price=float(trade['price']),
                        quantity=float(trade['qty']),
                        trade_time=datetime.fromtimestamp(trade['time']/1000),
                        side='BUY' if trade['isBuyerMaker'] else 'SELL',
                        trade_id=f"binance_{symbol}_{trade['id']}"
                    )
                    
                    try:
                        session.add(new_trade)
                        session.commit()
                    except:
                        session.rollback()
                        continue
            
            session.close()
            return True
            
        except Exception as e:
            print(f"Error fetching trades: {str(e)}")
            return False 