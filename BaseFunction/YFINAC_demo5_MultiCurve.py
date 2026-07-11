# 匯入必要的庫
import yfinance as yf
import matplotlib.pyplot as plt

# 定義股票代號
stock_code = "AAPL"

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
#收盤價走勢圖（Closing Price Chart）或線圖（Line Chart）
'''
    定義： 股票收盤價隨時間變化的圖表。
    用途： 描述股票價格走勢。
    繪製： 使用 plt.plot(hist.index, hist['Close']) 指令，以時間為 x 軸，收盤價為 y 軸繪製折線圖。
    解讀：
        呈現股票收盤價隨時間變動的趨勢。
        提供投資者分析股價變動的視覺化資訊。
'''
def plot_stock_data(hist):
    plt.figure(figsize=(12,6))
    plt.plot(hist.index, hist['Close'])
    plt.title('Closing Price')
    plt.xlabel('date')
    plt.ylabel('closing price')
    #顯示圖表，並設定圖表的副標題和網格線
    plt.grid(True)
    plt.suptitle(f'{stock_code} {hist.index[0].strftime("%Y-%m-%d")} ~ {hist.index[-1].strftime("%Y-%m-%d")}')
    plt.show()
# 交易量走勢圖（Volume Chart）或長條圖（Bar Chart）
'''
    定義： 顯示股票交易量隨時間變化的圖表。
    用途： 分析股票市場需求和供應，輔助投資決策。
    繪製： 使用 plt.bar(hist.index, hist['Volume']) 指令，以時間為 x 軸，交易量為 y 軸繪製條形圖。
    解讀：
        交易量增加可能預示股價上漲。
        交易量減少可能預示股價下跌。
'''
def plot_stock_volume(hist):
    plt.figure(figsize=(12,6))
    plt.bar(hist.index, hist['Volume'])
    plt.title('Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    #顯示圖表，並設定圖表的副標題和網格線
    plt.grid(True)
    plt.suptitle(f'{stock_code} {hist.index[0].strftime("%Y-%m-%d")} ~ {hist.index[-1].strftime("%Y-%m-%d")}')
    plt.show()
# 移動平均線（Moving Average）走勢圖
# 簡單移動平均線（Simple Moving Average）或滑動平均線（SMA）
'''
    定義： 股票收盤價在特定時間範圍內的平均值。
    用途： 平滑股價走勢，減少短期波動影響，幫助投資者識別長期趨勢。
    繪製： 使用 plt.plot(hist.index, ma_50) 和 plt.plot(hist.index, ma_200) 指令，分別繪製 50 日和 200 日移動平均線。
    解讀：
        當短期移動平均線（如 50 日）上穿長期移動平均線（如 200 日）時，可能是買入信號。
        當短期移動平均線下穿長期移動平均線時，可能是賣出信號。
'''
def plot_stock_ma(hist):
    '''
    計算股票收盤價的 50 日移動平均線和 200 日移動平均線
    rolling() 函數用於計算移動平均線，window 參數指定了移動平均線的時間窗口大小。
    '''
    ma_50 = hist['Close'].rolling(window=50).mean()
    ma_200 = hist['Close'].rolling(window=200).mean()

    plt.figure(figsize=(12,6))
    #繪製收盤價走勢圖
    plt.plot(hist.index, hist['Close'], label='Close')
    #繪製移動平均線走勢圖
    plt.plot(hist.index, ma_50, label='MA 50')
    plt.plot(hist.index, ma_200, label='MA 200')
    plt.title('Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    #繪製圖例，顯示不同線條的意義
    plt.legend()
    #顯示圖表，並設定圖表的副標題和網格線
    plt.grid(True)
    plt.suptitle(f'{stock_code} {hist.index[0].strftime("%Y-%m-%d")} ~ {hist.index[-1].strftime("%Y-%m-%d")}')
    plt.show()

# 呼叫畫圖函式
plot_stock_data(hist)
plot_stock_volume(hist)
plot_stock_ma(hist)