import numpy as np
import matplotlib.pyplot as plt

# 觀察資料
X = np.array([0, 2, 4, 6, 8])  # 吃炸雞次數／月
y = np.array([0, 0.5, 1.2, 2.0, 2.7])  # 體重增加（公斤）

# 計算線性回歸係數
# 使用最小平方法計算線性回歸的係數 b0 和 b1
# b0 是截距，b1 是斜率
# 公式：y = b0 + b1 * X
# 計算 X 和 y 的平均值，也就是資料的中心位置。
X_mean = np.mean(X)
y_mean = np.mean(y)
#計算**共變異數（covariance）**的分子部分。它反映的是：當 X 增加時，y 是不是也跟著增加？
numerator = np.sum((X - X_mean) * (y - y_mean))
#這是計算 X 的變異數，表示 X 自己的波動程度。
denominator = np.sum((X - X_mean) ** 2)
#計算斜率 b1，這是線性回歸的關鍵參數之一，表示 X 每增加一單位，y 會增加多少。
b1 = numerator / denominator
#計算截距 b0，這是線性回歸的另一個關鍵參數，表示當 X 為 0 時，y 的預測值。
b0 = y_mean - b1 * X_mean

# 預測新同學的體重增加
new_X = 5
new_y = b0 + b1 * new_X

# 計算紅線值
red_line_values = b0 + b1 * X

# 印出每個點對應的紅線值
print("每個點對應的紅線值:")
print(red_line_values)

# 印出線性回歸方程式
print("線性回歸方程式: y = {:.2f}x + {:.2f}".format(b1, b0))

# 畫出圖形
plt.scatter(X, y, label='Observed Data')
plt.plot(X, b0 + b1 * X, label='Linear Regression Line', color='red')
plt.scatter(new_X, new_y, label='Predicted Value', color='green')
plt.xlabel('Fried Chicken Consumption (times/month)')
plt.ylabel('Weight Gain (kg)')
plt.title('Linear Regression Analysis')
plt.legend()
plt.show()