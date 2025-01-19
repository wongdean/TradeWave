import time
from app.services.binance_service import BinanceService
from config.config import Config

def main():
    # 初始化已启用的交易所服务
    services = []
    if Config.EXCHANGES['binance']['enabled']:
        services.append(BinanceService())
    
    print("开始监控交易数据...")
    print(f"已启用的交易所：binance")
    print(f"监控的交易对：{', '.join(Config.EXCHANGES['binance']['symbols'])}")
    
    while True:
        try:
            for service in services:
                success = service.get_recent_trades()
                if success:
                    print(f"成功更新交易数据")
                else:
                    print(f"更新交易数据失败")
        except Exception as e:
            print(f"发生错误: {str(e)}")
        
        time.sleep(Config.UPDATE_INTERVAL)

if __name__ == "__main__":
    main() 