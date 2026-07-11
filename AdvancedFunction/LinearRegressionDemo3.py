import numpy as np
'''
這支程式產生了100筆的1維陣列作為訓練資料，
然後用LinearRegression模型預測X_new
為np.array([[0.5]])時的y_pred值是多少
'''
# 產生資料
# 設定 NumPy 的隨機種子為 0。這個設定可以確保 NumPy 的隨機數生成器產生相同的隨機數序列。
# 使用numpy隨機數生成器產生100個隨機數作為X，並根據y = 3X + 2 + 隨機噪聲生成y
# 這裡的隨機噪聲是從正態分佈中抽取的，標準差為1.5，這樣可以模擬真實世界中的一些隨機變化。
np.random.seed(0)
X = np.random.rand(100, 1)#100 筆、1 維特徵的資料。
#你可以把它想成：輸入一個數值（例如 0.5），模型會預測對應的結果（接近 3 × 0.5 + 2 = 3.5）。
y = 3 * X + 2 + np.random.randn(100, 1) / 1.5

# 訓練模型
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

# 預測
#這裡我們隨便選擇一個新的輸入數據 X_new（例如 0.5），然後使用訓練好的模型進行預測。
#模型會根據之前學到的參數（權重和偏差）來預測對應的 y 值。
X_new = np.array([[0.5]])
y_pred = model.predict(X_new)
print("預測結果：", y_pred)

# 評估模型
#這裡重新使用訓練資料 X 進行預測，與實際 y 進行比較，計算出模型的 均方誤差（MSE）。
#MSE 越小，代表模型預測越準確。
from sklearn.metrics import mean_squared_error
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
print("均方誤差：", mse)
# 使用模型進行預測
print("MSE：", mse)
'''
項目	   說明
資料筆數	100 筆
資料型態	X 和 y 都是 NumPy 陣列（ndarray）
資料維度	X 為 (100, 1)，y 為 (100, 1)
預測目標	線性關係：y ≈ 3 × X + 2 + 雜訊
預測結果	模型對 X=0.5 的資料進行預測
評估指標	使用 均方誤差（MSE） 評估模型準確度
'''