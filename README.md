# 加密货币交易数据采集

本项目主要语言为python，使用框架为flask，数据库为PostgreSQL。

## 功能
- [x] 支持多个交易所数据采集
- [x] 支持多个交易对监控
- [x] 数据存储到PostgreSQL数据库

## 支持的交易所
- [x] 币安（Binance）
- [x] OKX（欧易）
- [ ] 火币（Huobi）- 开发中
- [ ] 其他交易所 - 计划中

## 安装和使用

1. 安装项目：
```bash
# 安装项目依赖
pip install -r requirements.txt

# 安装项目（开发模式）
pip install -e .
```

2. 配置环境变量：
- 复制 `.env.example` 为 `.env`
- 填入交易所API密钥和数据库配置
- 配置需要监控的交易对（BINANCE_SYMBOLS）

3. 启动PostgreSQL数据库：
```bash
docker-compose up -d
```

4. 运行程序：
```bash
python3 run.py
```

## 数据库结构

trades表包含以下字段：
- id: 主键
- exchange: 交易所名称
- symbol: 交易对
- price: 价格
- quantity: 数量
- trade_time: 交易时间
- side: 交易方向（买/卖）
- trade_id: 交易ID

## 配置说明

在 `.env` 文件中可以配置：
- 数据库连接信息
- 交易所API密钥
- 监控的交易对列表
- 更新间隔
- 启用/禁用特定交易所

示例配置：
```env
# 数据库配置
DB_USER=crypto
DB_PASSWORD=crypto123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crypto_trades

# Binance配置
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
BINANCE_SYMBOLS=BTCUSDT,ETHUSDT,PUNTUSDT
BINANCE_ENABLED=true

# OKX配置
OKX_API_KEY=your_okx_api_key
OKX_API_SECRET=your_okx_api_secret
OKX_PASSPHRASE=your_okx_passphrase
OKX_SYMBOLS=BTC-USDT,ETH-USDT,PUNT-USDT
OKX_ENABLED=true

# 全局配置
UPDATE_INTERVAL=60
```

## 数据库管理

- 数据库文件存储在 `./data/postgres` 目录
- 可以使用任何PostgreSQL客户端连接数据库
- 默认连接信息：
  - 主机：localhost
  - 端口：5432
  - 数据库：crypto_trades
  - 用户名：crypto
  - 密码：crypto123

## 添加新的交易所

1. 在 `config/config.py` 中添加新的交易所配置
2. 在 `app/services` 目录下创建新的服务类
3. 在 `app/main.py` 中初始化新的服务

