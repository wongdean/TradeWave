# TradeWave

加密货币交易数据采集系统，支持多交易所实时交易数据获取和存储。

## 功能特性

- 多交易所支持：币安(Binance)、OKX
- 多交易对监控
- PostgreSQL 数据存储
- 实时数据更新

## 快速开始

### 第一步：配置 Python 环境

1. 使用 Conda 创建环境（推荐）：
```bash
# 创建新环境
conda create -n tradewave python=3.12 -y

# 激活环境
conda activate tradewave

# 安装依赖
pip install -r requirements.txt
pip install -e .
```

2. 或使用 venv（可选）：
```bash
# 创建环境
python -m venv venv

# 激活环境（Linux/Mac）
source venv/bin/activate
# Windows: .\venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
pip install -e .
```

### 第二步：配置数据库

1. 确保已安装 Docker 和 Docker Compose：
```bash
# 检查安装
docker --version
docker compose version
```

2. 复制环境变量模板：
```bash
cp .env.example .env
```

3. 配置数据库连接信息（默认无需修改）：
```env
# PostgreSQL配置
DB_USER=crypto
DB_PASSWORD=crypto123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crypto_trades
```

4. 启动数据库：
```bash
# 启动
docker compose up -d db

# 验证状态
docker compose ps
```

### 第三步：运行项目

1. 确保环境已激活：
```bash
conda activate tradewave
```

2. 确保启动脚本可执行：
```bash
chmod +x start.sh
```

3. 启动项目：
```bash
./start.sh
```

## 配置说明

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

## 常见问题

### 环境问题

1. conda 环境问题：
   - 确保正确安装了 conda
   - 使用 `conda env list` 检查环境
   - 如需重新创建：`conda env remove -n tradewave && conda create -n tradewave python=3.12 -y`

2. 依赖安装失败：
   - 确保环境已激活
   - 尝试：`pip install --no-cache-dir -r requirements.txt`

### 数据库问题

1. 数据库启动问题：
   - 检查 Docker 状态：`docker ps`
   - 查看日志：`docker compose logs -f db`
   - 端口冲突：修改 `docker-compose.yml` 中的端口映射

2. 数据库连接失败：
   - 确保容器运行：`docker compose ps`
   - 验证连接信息
   - 检查数据库日志：`docker compose logs -f db`

### 其他操作

1. 停止数据库：
```bash
# 停止并保留数据
docker compose stop db

# 停止并删除数据（谨慎使用）
docker compose down
```

2. 数据持久化：
   - 数据默认保存在 `./data/postgres` 目录
   - 确保目录具有正确的权限

