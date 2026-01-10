import tushare as ts
import pandas as pd
from datetime import datetime
import sys

print("Script started...")
print(f"Python version: {sys.version}")

# 股票代码映射 - 使用英文名称
STOCKS = {
    'Moutai': '600519.SH',
    'Wuliangye': '000858.SZ', 
    'GuotaiJunan': '601211.SH',
    'SMIC': '688981.SH'
}

# 日期范围
START_DATE = '2020-01-01'
END_DATE = datetime.now().strftime('%Y-%m-%d')

# 输出文件名
OUTPUT_FILE = f'stock_historical_data_{END_DATE}.xlsx'

def main():
    print("Entering main function...")
    
    # 设置tushare token
    token = '79639a75242c79e4dad87df7a8b1a88eef891f2f382fe7384133502a'
    print(f"Using token: {token[:10]}...")
    
    try:
        ts.set_token(token)
        print("Token set successfully")
    except Exception as e:
        print(f"Error setting token: {e}")
        return
    
    try:
        pro = ts.pro_api()
        print("API connected successfully")
    except Exception as e:
        print(f"Error connecting to API: {e}")
        return
    
    # 创建空的 DataFrame 来存储所有合并数据
    all_data = pd.DataFrame()
    
    print(f"开始获取股票数据 (从 {START_DATE} 到 {END_DATE})...")
    print("=" * 50)
    
    # 逐个获取股票数据
    for stock_name, stock_code in STOCKS.items():
        print(f"正在获取: {stock_name} ({stock_code})")
        
        try:
            print(f"Requesting data for {stock_code} from {START_DATE} to {END_DATE}")
            # 获取日线数据
            df = pro.daily(
                ts_code=stock_code,
                start_date=START_DATE.replace('-', ''),
                end_date=END_DATE.replace('-', '')
            )
            print(f"Data received: {df.shape}")
            
            if not df.empty:
                # 添加股票名称列
                df['stock_name'] = stock_name
                # 转换日期格式
                df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
                # 重命名列为英文
                df = df.rename(columns={
                    'ts_code': 'stock_code',
                    'open': 'open',
                    'high': 'high',
                    'low': 'low',
                    'close': 'close',
                    'pre_close': 'pre_close',
                    'change': 'change',
                    'pct_chg': 'pct_chg',
                    'vol': 'volume',
                    'amount': 'amount'
                })
                
                # 追加到总数据
                all_data = pd.concat([all_data, df], ignore_index=True)
                print(f"✅ {stock_name} 数据获取成功，共 {len(df)} 条记录")
            else:
                print(f"❌ {stock_name} 没有数据")
                
        except Exception as e:
            print(f"❌ 获取 {stock_name} 数据失败: {str(e)}")
            import traceback
            traceback.print_exc()
    
    # 按 trade_date 从大到小排序
    if not all_data.empty:
        all_data = all_data.sort_values('trade_date', ascending=False)
        print(f"\n所有数据已合并，共 {len(all_data)} 条记录")
        
        # 保存到单个 Excel 工作表
        try:
            with pd.ExcelWriter(OUTPUT_FILE, engine='openpyxl') as writer:
                all_data.to_excel(writer, sheet_name='All_Symbols', index=False)
            print(f"Excel file saved successfully to {OUTPUT_FILE}")
        except Exception as e:
            print(f"Error saving Excel file: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("❌ 没有获取到任何数据")
    
    print("=" * 50)
    print(f"\n✅ 所有数据已保存到: {OUTPUT_FILE}")
    print("Script completed successfully")

if __name__ == "__main__":
    main()