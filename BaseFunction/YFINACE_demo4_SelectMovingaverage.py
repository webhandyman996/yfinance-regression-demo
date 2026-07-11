# 匯入必要的庫
import yfinance as yf
import matplotlib.pyplot as plt

# 定義股票代號選擇介面
def select_stock_code():
    print("請選擇股票代號：")
    print("1. Apple (AAPL)")
    print("2. Google (GOOG)")
    print("3. Amazon (AMZN)")
    print("4. Microsoft (MSFT)")
    print("5. 自行輸入股票代號")
    
    choice = input("請輸入選擇（1-5）：")
    
    if choice == "1":
        stock_code = "AAPL"
    elif choice == "2":
        stock_code = "GOOG"
    elif choice == "3":
        stock_code = "AMZN"
    elif choice == "4":
        stock_code = "MSFT"
    elif choice == "5":
        stock_code = input("請輸入股票代號：")
    else:
        print("無效選擇，請重新選擇。")
        return select_stock_code()
    
    return stock_code
# 定義日期區間選擇介面
def select_date_range():
    print("請選擇日期區間：")
    print("1. 1天")
    print("2. 1周")
    print("3. 1個月")
    print("4. 3個月")
    print("5. 6個月")
    print("6. 1年")
    print("7. 自行輸入日期區間")
    
    choice = input("請輸入選擇（1-7）：")
    
    if choice == "1":
        period = "1d"
    elif choice == "2":
        period = "1wk"
    elif choice == "3":
        period = "1mo"
    elif choice == "4":
        period = "3mo"
    elif choice == "5":
        period = "6mo"
    elif choice == "6":
        period = "1y"
    elif choice == "7":
        start_date = input("請輸入開始日期（YYYY-MM-DD）：")
        end_date = input("請輸入結束日期（YYYY-MM-DD）：")
        period = f"{start_date}/{end_date}"
    else:
        print("無效選擇，請重新選擇。")
        return select_date_range()
    
    return period

# 取得股票代號
stock_code = select_stock_code()

# 取得股票資料
stock_data = yf.Ticker(stock_code)

# 取得股票基本資料
print("stock Name:", stock_data.info['shortName'])
print("stock ID：", stock_code)
print("stock Value：", stock_data.info['currentPrice'])

# 取得日期區間
period = select_date_range()
# 取得股票歷史資料
if "/" in period:
    start_date, end_date = period.split("/")
    hist = stock_data.history(start=start_date, end=end_date)
else:
    hist = stock_data.history(period=period)
    
# 印出股票歷史資料
print(hist)

# 定義畫圖函式
def plot_stock_data(hist):
    plt.figure(figsize=(12,6))
    plt.plot(hist.index, hist['Close'])
    plt.title('Closing Price')
    plt.xlabel('date')
    plt.ylabel('closing price')
    plt.grid(True)
    plt.suptitle(f'{stock_code} {hist.index[0].strftime("%Y-%m-%d")} ~ {hist.index[-1].strftime("%Y-%m-%d")}')
    plt.show()

# 呼叫畫圖函式
plot_stock_data(hist)