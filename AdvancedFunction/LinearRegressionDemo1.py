import numpy as np
import matplotlib.pyplot as plt

# 觀察資料
X = np.array([1, 2, 3, 4, 5])  # 唸書時間（小時）
y = np.array([55, 60, 67, 73, 80])  # 考試分數

# 預測新同學的考試分數
new_X = 3.5
new_y = 5 * new_X + 50 + (new_X -2) # 使用公式計算預測分數


# 計算紅線值
red_line_values = 5 * X + 50 + (X - 2)

# 印出每個點對應的紅線值
print("每個點對應的紅線值:")
print(red_line_values)

# 畫出圖形
plt.scatter(X, y, label='Observed data', color='blue')
plt.plot(X, 5 * X + 50 + (X-2), label='Linear regression', color='red')
plt.scatter(new_X, new_y, label='Prediect value', color='green')
plt.xlabel('Reading time（hoiurs）')
plt.ylabel('score')
plt.title('Reading time vs. score')
plt.legend()
plt.show()