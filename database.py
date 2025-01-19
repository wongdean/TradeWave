from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import Config
from app.models.trade import Trade
import logging

class Database:
    def __init__(self):
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        
    def save_trades(self, trades):
        """保存交易数据到数据库"""
        session = self.Session()
        try:
            for trade_data in trades:
                trade = Trade(
                    exchange=trade_data['exchange'],
                    symbol=trade_data['symbol'],
                    price=trade_data['price'],
                    quantity=trade_data['quantity'],
                    trade_time=trade_data['trade_time'],
                    side=trade_data['side'],
                    trade_id=trade_data['trade_id']
                )
                session.add(trade)
            session.commit()
            return True
        except Exception as e:
            logging.error(f"Error saving trades: {str(e)}")
            session.rollback()
            return False
        finally:
            session.close() 