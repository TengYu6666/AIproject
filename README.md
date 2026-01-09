# 股票历史数据下载与分析工具

## 📌 项目说明

这是一个完整的股票数据处理系统，包括数据下载、存储、查询和分析功能。它使用 Python、tushare 库获取股票历史数据，并结合 AI 助手技术提供智能分析和可视化。

## ✨ 主要功能

1. **数据下载**: 使用 tushare 获取四只主要股票的历史价格数据
2. **数据存储**: 支持 Excel 导出和 MySQL 数据库存储
3. **AI 分析助手**: 基于 qwen-agent 的智能股票查询分析
4. **数据可视化**: 自动生成股票价格趋势图和统计图表
5. **多界面支持**: 同时提供终端交互和 Web 图形界面
6. **BI 分析功能**: 支持复杂的 SQL 查询和数据分析

## 📊 支持的股票

- 贵州茅台 (600519.SH)
- 五粮液 (000858.SZ)
- 国泰君安 (601211.SH)
- 中芯国际 (688981.SH)

## 📅 数据范围

- 起始日期：2020-01-01
- 结束日期：当前日期

## 🚀 使用方法

### 1. 环境准备

安装 Python 3.7+ 环境

### 2. 安装依赖包

```bash
pip install -r requirements.txt
```

### 3. 获取 tushare token

如需运行数据下载功能：
- 访问 [tushare.pro](https://tushare.pro/)
- 注册账号
- 在个人主页获取 token
- 在 `stock_data_downloader.py` 中配置 token

### 4. 配置 MySQL 数据库

如需运行 AI 分析助手，需配置 MySQL 连接：
- 创建数据库 `stock_data`
- 在 `stock_analysis_assistant.py` 和 `import_excel_to_mysql.py` 中更新连接信息

### 5. 数据下载

```bash
python stock_data_downloader.py
```

### 6. 数据导入（可选）

将 Excel 数据导入到 MySQL 数据库：

```bash
python import_excel_to_mysql.py
```

### 7. 启动股票分析助手

**方式一：图形界面（推荐）**
```bash
python stock_analysis_assistant.py
```

**方式二：命令行模式**
在 `stock_analysis_assistant.py` 中将 main 函数中的 `app_gui()` 改为 `app_tui()`

**方式三：一键运行（Windows）**
- 双击 `run.bat` 运行
- 或者运行 `run.ps1`（PowerShell）

## 📁 输出结果

### 数据文件
- `stock_historical_data_YYYY-MM-DD.xlsx` - 完整的股票历史数据
- MySQL 数据库表 `stock_historical_data` - 结构化数据存储

### 分析结果
- `stock_charts/` 目录 - 自动生成的股票分析图表
- 智能分析报告 - 通过 AI 助手输出

## 📋 数据字段说明

- **stock_code**：股票代码
- **stock_name**：股票名称
- **trade_date**：交易日期（YYYY-MM-DD 格式）
- **open**：开盘价
- **high**：最高价
- **low**：最低价
- **close**：收盘价
- **pre_close**：前一个交易日收盘价
- **change**：当日涨跌额
- **pct_chg**：当日涨跌幅（%）
- **volume**：成交量（手）
- **amount**：成交额（万元）

## ⚠️ 注意事项

- 使用 tushare 库需要有网络连接
- AI 分析功能需要配置 DashScope API Key
- 部分功能可能需要 tushare 的积分
- 合理使用避免频繁请求导致服务限制
- MySQL 连接需要正确配置用户名和密码

## 📞 联系方式

如有问题，请参考 tushare 和 qwen-agent 官方文档或在其社区提问