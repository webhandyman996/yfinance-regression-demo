#YFINACE的範例程式
# 匯入必要的庫
import yfinance as yf

# 定義股票代號
stock_code = "AAPL"

# 取得股票資料
'''
    定義： 使用 yfinance 資料庫的 Ticker 函式取得指定股票的資料。
    用途： 提供股票的基本資料、歷史價格等資訊。
    繪製： 使用 yf.Ticker(stock_code) 指令取得股票資料。
    解讀：
        stock_data.info 提供股票的基本資訊，如名稱、價格等。
        stock_data.history(period="1y") 提供過去一年內的歷史價格資料。
        hist.index 提供資料的日期索引。
'''
stock_data = yf.Ticker(stock_code)

# 取得股票基本資料
# stock_data.info 提供股票的基本資訊，如名稱、價格等。
#stock_code 提供股票的代號。
# stock_data.info['currentPrice'] 提供股票的當前價格。
print("股票名稱：", stock_data.info['shortName'])
print("股票代號：", stock_code)
print("股票價格：", stock_data.info['currentPrice'])

# 取得股票歷史資料
hist = stock_data.history(period="1y")

# 印出股票歷史資料
print(hist)
