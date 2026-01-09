import pandas as pd
import os

# 设置工作目录
work_dir = r"e:\大模型实操\交互式BI报表"
file_path = os.path.join(work_dir, "stock_historical_data_2025-12-26.xlsx")

if os.path.exists(file_path):
    print(f"正在读取 Excel 文件: {file_path}")
    
    # 读取 Excel 文件数据
    df = pd.read_excel(file_path, sheet_name="All_Symbols")
    
    print("\n=== Excel 表结构信息 ===")
    print(f"总行数: {len(df)}")
    print(f"列数: {len(df.columns)}")
    print(f"\n字段列表 (Excel 表头):")
    
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
        # 获取字段数据类型
        print(f"   数据类型: {df[col].dtype}")
        # 显示前几个数据样本
        print(f"   样本数据: {df[col].head().tolist()}")
        print()
    
    print("\n=== 数据前 5 行 ===")
    print(df.head())
    
    print("\n=== 验证 SQL 语句字段对应关系 ===")
    print("\nSQL 表字段:")
    print("id (自增主键)")
    print("stock_code")
    print("stock_name")
    print("trade_date")
    print("open")
    print("high")
    print("low")
    print("close")
    print("pre_close")
    print("change")
    print("pct_chg")
    print("volume")
    print("amount")
    
    print("\n=== 字段对应关系检查 ===")
    sql_fields = ["stock_code", "stock_name", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "volume", "amount"]
    
    missing_fields = []
    extra_fields = []
    
    for sql_field in sql_fields:
        if sql_field not in df.columns:
            missing_fields.append(sql_field)
    
    for excel_field in df.columns:
        if excel_field not in sql_fields:
            extra_fields.append(excel_field)
    
    print(f"Missing fields (Excel 中缺失的 SQL 字段): {missing_fields}")
    print(f"Extra fields (Excel 中多出的字段): {extra_fields}")
    
    if not missing_fields and not extra_fields:
        print("✅ 所有字段都匹配！")
    else:
        print("❌ 字段匹配有差异！")
    
else:
    print(f"文件不存在: {file_path}")