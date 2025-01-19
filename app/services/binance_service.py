from datetime import datetime
from binance.client import Client
from typing import List, Dict
import logging

class BinanceService:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        
    def get_trades(self, symbol: str, limit: int = 100) -> List[Dict]:
        """获取最近的交易数据"""
        try:
            # 将 BTC-USDT 转换为 BTCUSDT 格式
            formatted_symbol = symbol.replace('-', '')
            trades_data = self.client.get_recent_trades(symbol=formatted_symbol, limit=limit)
            trades = []
            
            for trade in trades_data:
                trades.append({
                    'exchange': 'binance',
                    'symbol': symbol,  # 保持原始格式
                    'price': float(trade['price']),
                    'quantity': float(trade['qty']),
                    'trade_time': datetime.fromtimestamp(trade['time']/1000),
                    'side': 'sell' if trade['isBuyerMaker'] else 'buy',
                    'trade_id': str(trade['id'])
                })
            return trades
                
        except Exception as e:
            logging.error(f"Error fetching trades from Binance: {str(e)}")
            return []

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