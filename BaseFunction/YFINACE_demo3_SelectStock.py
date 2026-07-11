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

# 取得股票代號
stock_code = select_stock_code()

# 取得股票資料
stock_data = yf.Ticker(stock_code)

# 取得股票基本資料
print("stock Name:", stock_data.info['shortName'])
print("stock ID：", stock_code)
print("stock Value：", stock_data.info['currentPrice'])

# 取得股票歷史資料
hist = stock_data.history(period="1y")

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