from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, UniqueConstraint, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import Config

Base = declarative_base()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    exchange = Column(String(20), nullable=False)  # 交易所名称
    symbol = Column(String(20), nullable=False)
    price = Column(Numeric(20, 10), nullable=False)
    quantity = Column(Numeric(20, 10), nullable=False)
    trade_time = Column(DateTime, nullable=False)
    side = Column(String(10), nullable=False)  # buy or sell
    trade_id = Column(String(50), nullable=False)
    
    __table_args__ = (
        UniqueConstraint('exchange', 'trade_id', name='uix_exchange_trade_id'),
    )
    
    def __init__(self, exchange, symbol, price, quantity, trade_time, side, trade_id):
        self.exchange = exchange
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        self.trade_time = trade_time
        self.side = side.lower()  # 统一转换为小写
        self.trade_id = trade_id

# 创建数据库表
Base.metadata.create_all(engine) 