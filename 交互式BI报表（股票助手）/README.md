# 📊 股票智能分析助手

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Data-Tushare-orange.svg" alt="Data Source">
  <img src="https://img.shields.io/badge/AI-Qwen--Agent-purple.svg" alt="AI Assistant">
  <img src="https://img.shields.io/badge/Visualization-Matplotlib-brightgreen.svg" alt="Visualization">
</div>

## 📌 项目说明

这是一个功能完整的股票数据智能处理与分析系统，集成了数据获取、存储、查询、分析和可视化功能。系统采用 Python 开发，利用 tushare 库获取股票历史数据，并结合 AI 技术提供智能分析服务，帮助投资者更好地理解股票市场趋势。

## ✨ 主要功能

### 📥 数据获取
- 使用 tushare API 获取股票历史价格数据
- 支持自定义股票列表扩展
- 自动更新数据至最新交易日

### 💾 数据存储
- 支持 Excel 格式导出与保存
- 兼容 MySQL 数据库存储
- 数据字段完整，便于后续分析

### 🤖 智能分析
- 基于 qwen-agent 的 AI 分析助手
- 支持自然语言查询股票信息
- 提供智能数据分析与解读
- **📉 ARIMA 价格预测**：使用 ARIMA 模型预测股票未来 N 天价格
- **📊 MACD 交易策略**：基于 MACD 指标分析股票买卖点和收益率
- **📰 Tavily 新闻搜索**：获取最新股票相关新闻
- **📚 RAG 知识库**：从本地 FAQ 知识库获取股票知识

### 📈 可视化呈现
- 自动生成股票价格趋势图
- 支持多股票对比分析
- 直观展示成交量与涨跌幅
- ARIMA 预测结果可视化
- MACD 交易策略图表

### 🖥️ 多界面支持
- **Web 界面 (WebUI)**：基于 qwen-agent 的 Web 界面，功能丰富，推荐使用
- **图形界面 (GUI)**：直观易用，适合普通用户
- **终端界面 (TUI)**：轻量级，适合高级用户
- **一键运行**：Windows 环境下支持双击运行

### 📊 BI 分析
- 支持复杂 SQL 查询
- 提供多维度数据统计
- 生成专业分析报告

## 🛠️ 技术栈

- **核心语言**: Python 3.7+
- **数据来源**: tushare.pro API
- **AI 框架**: qwen-agent
- **可视化库**: Matplotlib、Pandas
- **数据库**: MySQL
- **GUI 框架**: 自定义图形界面
- **其他库**: openpyxl、pymysql

## 📊 默认支持股票

- 贵州茅台 (600519.SH)
- 五粮液 (000858.SZ)
- 国泰君安 (601211.SH)
- 中芯国际 (688981.SH)

## 📅 数据范围

- 起始日期：2020-01-01
- 结束日期：自动更新至当前日期

## 🚀 快速开始

### 1. 环境准备

确保已安装 Python 3.7 或更高版本：

```bash
python --version
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 获取 tushare Token

如需使用数据下载功能：

1. 访问 [tushare.pro](https://tushare.pro/)
2. 注册账号并登录
3. 在个人主页获取 Token
4. 在 `stock_data_downloader.py` 中配置 Token

### 4. 配置 MySQL 数据库（可选）

如需使用 AI 分析助手功能：

1. 安装并启动 MySQL 服务
2. 创建数据库：`CREATE DATABASE stock_data;
3. 在以下文件中更新数据库连接信息：
   - `stock_analysis_assistant.py`
   - `import_excel_to_mysql.py`

### 5. 数据下载

```bash
python stock_data_downloader.py
```

### 6. 数据导入（可选）

将 Excel 数据导入到 MySQL 数据库：

```bash
python import_excel_to_mysql.py
```

### 7. 启动分析助手

#### 🌐 Web 界面（推荐）

```bash
python stock_analysis_assistant.py
```

系统将自动启动 Web 服务器，在浏览器中访问提示的地址（通常为 http://localhost:8000）即可使用。

#### 🖱️ 图形界面

```bash
python stock_analysis_assistant.py
```

#### 📟 命令行模式

在 `stock_analysis_assistant.py` 中将 `app_gui()` 或 `app_webui()` 改为 `app_tui()`：

```python
if __name__ == "__main__":
    app_tui()  # 改为终端界面
```

然后运行：

```bash
python stock_analysis_assistant.py
```
## 📁 项目结构

```
.
├── stock_data_downloader.py         # 数据下载模块
├── import_excel_to_mysql.py         # 数据导入模块
├── stock_analysis_assistant.py      # 智能分析助手
├── faq.txt                          # RAG 知识库数据源
├── requirements.txt                 # 依赖列表
└── README.md                        # 项目说明文档
```

## 📁 输出结果

### 数据文件
- `stock_historical_data_YYYY-MM-DD.xlsx` - 完整的股票历史数据
- MySQL 数据库表 `stock_historical_data` - 结构化数据存储

### 分析结果
- `stock_charts/` 目录 - 自动生成的股票分析图表
- 智能分析报告 - 通过 AI 助手输出

## 📋 数据字段说明

| 字段名 | 说明 | 格式 |
|--------|------|------|
| stock_code | 股票代码 | 字符串（如：600519.SH） |
| stock_name | 股票名称 | 字符串（如：贵州茅台） |
| trade_date | 交易日期 | YYYY-MM-DD |
| open | 开盘价 | 浮点数 |
| high | 最高价 | 浮点数 |
| low | 最低价 | 浮点数 |
| close | 收盘价 | 浮点数 |
| pre_close | 前收盘价 | 浮点数 |
| change | 涨跌额 | 浮点数 |
| pct_chg | 涨跌幅 | 百分比（%） |
| volume | 成交量 | 手 |
| amount | 成交额 | 万元 |

## ⚠️ 注意事项

- 使用 tushare API 需要网络连接和积分
- AI 分析功能需要配置 **DashScope API Key**（通义千问）
- **Tavily 新闻搜索**需要配置 **TAVILY_API_KEY**
- 部分高级数据接口需要 tushare 积分
- 请合理使用 API，避免频繁请求导致服务限制
- MySQL 连接需要正确配置用户名和密码

### 📝 环境变量配置说明

所有API密钥和数据库连接参数都需要通过环境变量配置：

#### Windows 系统
```powershell
# 设置 DashScope API Key（通义千问）
setx DASHSCOPE_API_KEY "your_dashscope_api_key"

# 设置 Tavily API Key（新闻搜索）
setx TAVILY_API_KEY "your_tavily_api_key"

# 设置 MySQL 连接参数
setx MYSQL_USER "root"
setx MYSQL_PASSWORD "your_mysql_password"  # 必填，无默认值
setx MYSQL_HOST "localhost"                # 可选，默认 localhost
setx MYSQL_PORT "3306"                    # 可选，默认 3306
```

#### Linux/macOS 系统
```bash
# 设置 DashScope API Key（通义千问）
export DASHSCOPE_API_KEY="your_dashscope_api_key"

# 设置 Tavily API Key（新闻搜索）
export TAVILY_API_KEY="your_tavily_api_key"

# 设置 MySQL 连接参数
export MYSQL_USER="root"
export MYSQL_PASSWORD="your_mysql_password"  # 必填，无默认值
export MYSQL_HOST="localhost"                # 可选，默认 localhost
export MYSQL_PORT="3306"                    # 可选，默认 3306

# 或者将这些设置添加到 ~/.bashrc 或 ~/.zshrc 文件中以永久生效
```

### 🔒 安全提示

- **请勿在代码中硬编码API密钥**，始终使用环境变量
- **MySQL密码不能为空**，必须通过环境变量设置
- **定期更换API密钥**以提高安全性
- **保护好环境变量**，避免在公共场合泄露

## 🤝 贡献指南

欢迎对项目进行贡献！贡献方式包括：

1. **报告问题**：在 GitHub Issues 中提交 bug 报告或功能建议
2. **代码贡献**：
   - Fork 项目
   - 创建特性分支：`git checkout -b feature/AmazingFeature`
   - 提交更改：`git commit -m 'Add some AmazingFeature'`
   - 推送到分支：`git push origin feature/AmazingFeature`
   - 提交 Pull Request
3. **文档完善**：帮助改进 README 或其他文档

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源，详见 LICENSE 文件。

## 🙏 致谢

- [tushare](https://tushare.pro/)：提供股票数据 API
- [qwen-agent](https://github.com/QwenLM/qwen-agent)：提供 AI 助手技术支持
- [Matplotlib](https://matplotlib.org/)：提供数据可视化支持

- [Pandas](https://pandas.pydata.org/)：提供数据处理功能
