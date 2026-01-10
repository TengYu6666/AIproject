-- 创建股票历史数据表的SQL语句
-- 适用于 MySQL 数据库
-- 表结构根据 stock_historical_data_*.xlsx 文件设计

CREATE TABLE `stock_historical_data` (
    `id` INT AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID，自增',
    `stock_code` VARCHAR(20) NOT NULL COMMENT '股票代码，格式如：600519.SH, 000858.SZ',
    `stock_name` VARCHAR(50) NOT NULL COMMENT '股票名称，英文名称',
    `trade_date` VARCHAR(10) NOT NULL COMMENT '交易日期，格式如：YYYYMMDD 或 YYYY-MM-DD',
    `open` DECIMAL(10, 2) NOT NULL COMMENT '开盘价',
    `high` DECIMAL(10, 2) NOT NULL COMMENT '最高价',
    `low` DECIMAL(10, 2) NOT NULL COMMENT '最低价',
    `close` DECIMAL(10, 2) NOT NULL COMMENT '收盘价',
    `pre_close` DECIMAL(10, 2) NOT NULL COMMENT '前一日收盘价',
    `change` DECIMAL(10, 2) NOT NULL COMMENT '涨跌额',
    `pct_chg` DECIMAL(10, 2) NOT NULL COMMENT '涨跌幅（%）',
    `volume` BIGINT NOT NULL COMMENT '成交量（手）',
    `amount` DECIMAL(15, 2) NOT NULL COMMENT '成交额（万元）',
    
    -- 添加唯一索引以避免重复数据
    UNIQUE KEY `uk_stock_date` (`stock_code`, `trade_date`),
    
    -- 添加索引以优化查询
    INDEX `idx_stock_code` (`stock_code`),
    INDEX `idx_trade_date` (`trade_date`),
    INDEX `idx_stock_name` (`stock_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='股票历史交易数据表';

-- 使用说明：
-- 1. 该表结构适用于 MySQL 数据库
-- 2. 可以根据实际使用的数据库（如 PostgreSQL、SQL Server）调整字段类型和语法
-- 3. 导入 Excel 数据时，建议使用数据库管理工具（如 MySQL Workbench、Navicat）的导入功能
-- 4. 或者使用 LOAD DATA INFILE 命令导入 CSV 格式数据
-- 5. 确保 Excel 中的数据格式与表结构一致，特别是日期格式
-- 6. 股票代码和交易日期组合为唯一索引，避免重复记录