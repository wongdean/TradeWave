# TradeWave

加密货币交易数据采集系统，支持多交易所实时交易数据获取和存储。

## 功能特性

- 多交易所支持：币安(Binance)、OKX
- 多交易对监控
- PostgreSQL 数据存储
- 实时数据更新

## 环境配置

### 方式一：使用 Conda（推荐）

```bash
# 创建新环境
conda create -n tradewave python=3.12 -y

# 激活环境
conda activate tradewave

# 切换环境（如果需要）
conda deactivate  # 先退出当前环境
conda activate tradewave  # 再激活目标环境

# 删除环境（如果需要）
conda deactivate
conda env remove -n tradewave
```

### 方式二：使用 venv

```bash
# 创建环境
python -m venv venv

# 激活环境
# Linux/Mac:
source venv/bin/activate
# Windows:
# .\venv\Scripts\activate

# 退出环境
deactivate
```

## 项目运行

1. 确保环境已激活：
```bash
# conda用户
conda activate tradewave

# venv用户
source venv/bin/activate  # Linux/Mac
# 或
# .\venv\Scripts\activate  # Windows
```

2. 首次运行配置：
```bash
# 确保启动脚本可执行
chmod +x start.sh

# 复制环境变量模板
cp .env.example .env

# 编辑环境变量
vim .env  # 或使用其他编辑器
```

3. 启动项目：
```bash
./start.sh  # 推荐
# 或
bash start.sh
```

注意：不要使用 `sh start.sh`，这可能导致环境变量问题。

## 项目配置

### 数据库配置

```env
# PostgreSQL配置
DB_USER=crypto
DB_PASSWORD=crypto123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crypto_trades
```

### 交易所配置

1. 币安(Binance)：
```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
BINANCE_SYMBOLS=BTC-USDT,ETH-USDT
BINANCE_ENABLED=true
```

2. OKX：
```env
OKX_API_KEY=your_okx_api_key
OKX_API_SECRET=your_okx_api_secret
OKX_PASSPHRASE=your_okx_passphrase
OKX_SYMBOLS=BTC-USDT,ETH-USDT
OKX_ENABLED=true
```

### 全局配置

```env
# 数据更新间隔（秒）
UPDATE_INTERVAL=60
```

## 数据说明

### 数据库表结构

trades表字段说明：
- id: 主键
- exchange: 交易所名称
- symbol: 交易对
- price: 价格
- quantity: 数量
- trade_time: 交易时间
- side: 交易方向（买/卖）
- trade_id: 交易ID

### 数据访问

默认数据库连接信息：
- 主机：localhost
- 端口：5432
- 数据库：crypto_trades
- 用户名：crypto
- 密码：crypto123

## 常见问题

1. 环境激活失败
   - 检查是否正确安装了 conda 或 Python
   - 确保使用了正确的激活命令

2. 依赖安装失败
   - 确保环境已正确激活
   - 检查网络连接
   - 尝试使用 `pip install --no-cache-dir -r requirements.txt`

3. 数据库连接失败
   - 确保 PostgreSQL 服务已启动
   - 验证数据库连接信息是否正确
   - 检查数据库用户权限

4. 交易所API连接失败
   - 验证API密钥是否正确
   - 检查网络连接
   - 确认API权限是否足够

