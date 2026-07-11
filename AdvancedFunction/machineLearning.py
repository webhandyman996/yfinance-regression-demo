import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
程式目的： 使用線性回歸（Linear Regression）來預測股票的收盤價。
取得股票資料（AAPL）
資料預處理：將日期轉換成時間戳，將收盤價縮小 100 倍
特徵工程：計算 5 日移動平均、20 日移動平均和相對強弱指標（RSI）
切割資料為訓練集和測試集
訓練線性回歸模型
預測股價
畫出預測值和實際值的圖形
'''
# 取得股票資料
stock_data = yf.Ticker("AAPL")
hist = stock_data.history(period="1y")

'''
 資料預處理
'''
#把資料框 hist 的索引（通常是日期）複製到名為 Date 的新欄位中，方便後續操作。
hist['Date'] = hist.index
#將 Date 欄位中的每個日期轉換成時間戳（從 1970 年 1 月 1 日 UTC 起的秒數），便於做數值運算與分析。
hist['Date'] = hist['Date'].apply(lambda x: x.timestamp())
#將 Close 欄位中的每個收盤價數值縮小 100 倍，這通常是為了統一單位或降低數值尺度以便處理。
hist['Close'] = hist['Close'].apply(lambda x: x / 100)

'''
# 特徵工程
'''
#計算的是 5 日移動平均（MA_5），也就是連續 5 天的收盤價平均值，用來平滑短期價格波動。
hist['MA_5'] = hist['Close'].rolling(window=5).mean()
#計算的是 20 日移動平均（MA_20），也就是連續 20 天的收盤價平均值，用來平滑長期價格波動。
hist['MA_20'] = hist['Close'].rolling(window=20).mean()
#計算相對強弱指標（RSI），透過收盤價的日漲跌幅與前一天的收盤價做比，衡量股價的上升或下跌動能。
hist['RSI'] = hist['Close'].diff(1) / hist['Close'].shift(1)

# 移除包含 NaN 值的列
hist = hist.dropna()

'''
切割資料為訓練集和測試集
'''
#從資料中選出三個特徵：5 日均線、20 日均線和 RSI，作為模型的輸入變數。
X = hist[['MA_5', 'MA_20', 'RSI']]
#從資料中選出收盤價作為模型的輸出變數。
y = hist['Close'].values

# 檢查 X 和 y 的長度
if len(X) == 0 or len(y) == 0:
    print("No data available")
else:
    # 切割資料為訓練集和測試集
    '''
    train_test_split 是 scikit-learn 提供的函式，用來將資料分為訓練集和測試集。
    主要參數：
    X：特徵資料（例如：MA_5、MA_20、RSI）
    y：目標資料（例如：收盤價）
    test_size=0.2：測試集佔全部資料的 20%
    random_state=42：設定隨機種子，確保每次切割結果一致

    回傳結果：
    X_train、y_train：訓練用的特徵與標籤
    X_test、y_test：測試用的特徵與標籤
    作用說明：
    這個函式的目的是把資料分成訓練用（80%）與驗證用（20%），讓模型能在學習後進行效果評估，避免過擬合或偏差。
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 訓練模型
    '''
    讓模型根據訓練資料進行學習。模型會自動找出最適合的權重（weights）和偏差（bias），
    讓預測值盡可能接近實際值，通常是透過最小化均方誤差來完成。
    '''
    #LinearRegression 是 scikit-learn 提供的線性迴歸模型，用來預測連續數值。
    #訓練線性回歸模型，目的是學會如何用特徵（X）來預測目標（y）。
    model = LinearRegression()
    #這行是建立一個線性回歸模型的實例。訓練模型，讓它根據訓練資料學習如何預測股價。
    model.fit(X_train, y_train)

    # 預測股價
    # 將測試集的特徵資料 X_test 傳入模型，模型會根據先前學到的參數（權重與偏差）進行預測，產出對應的股價結果。
    y_pred = model.predict(X_test)

    # 畫圖
    plt.figure(figsize=(12,6))
    plt.plot(y_test, label='Actual')
    plt.plot(y_pred, label='Predicted')
    plt.title('Closing Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()