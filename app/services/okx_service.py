import time
import hmac
import base64
import json
from datetime import datetime
import requests
from typing import List, Dict
import logging

class OKXService:
    def __init__(self, api_key: str, api_secret: str, passphrase: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase
        self.base_url = "https://www.okx.com"
        
    def _get_timestamp(self):
        return datetime.utcnow().isoformat()[:-3] + 'Z'

    def _sign(self, timestamp: str, method: str, request_path: str, body: str = ''):
        message = timestamp + method + request_path + (body or '')
        mac = hmac.new(
            bytes(self.api_secret, encoding='utf8'),
            bytes(message, encoding='utf-8'),
            digestmod='sha256'
        )
        d = mac.digest()
        return base64.b64encode(d).decode()

    def _get_header(self, method: str, request_path: str, body: str = ''):
        timestamp = self._get_timestamp()
        sign = self._sign(timestamp, method, request_path, body)
        
        return {
            'OK-ACCESS-KEY': self.api_key,
            'OK-ACCESS-SIGN': sign,
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        }

    def get_trades(self, symbol: str, limit: int = 100) -> List[Dict]:
        """获取最近的交易数据"""
        endpoint = f"/api/v5/market/trades"
        params = {'instId': symbol, 'limit': limit}
        
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                params=params,
                headers=self._get_header('GET', endpoint)
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get('code') == '0':
                trades = []
                for trade in data.get('data', []):
                    trades.append({
                        'exchange': 'okx',
                        'symbol': symbol,
                        'price': float(trade['px']),
                        'quantity': float(trade['sz']),
                        'trade_time': datetime.fromtimestamp(float(trade['ts']) / 1000),
                        'side': 'buy' if trade['side'] == 'buy' else 'sell',
                        'trade_id': trade['tradeId']
                    })
                return trades
            else:
                logging.error(f"OKX API error: {data}")
                return []
                
        except Exception as e:
            logging.error(f"Error fetching trades from OKX: {str(e)}")
            return [] 