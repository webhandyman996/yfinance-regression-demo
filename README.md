# yfinance 股票資料與回歸應用教學範例

機器學習課程教學範例，示範如何用 `yfinance` 取得股票資料，並將回歸方法應用在真實股價預測上。

## `BaseFunction/`：yfinance 基礎操作

| 檔案 | 說明 |
| --- | --- |
| YFINACE_demo1_Getdata.py | 取得股票資料 |
| YFINACE_demo2_DrawChart.py | 畫出股價走勢圖 |
| YFINACE_demo3_SelectStock.py | 選擇特定股票 |
| YFINACE_demo4_SelectMovingaverage.py | 計算移動平均線 |
| YFINAC_demo5_MultiCurve.py | 多條曲線比較 |

## `AdvancedFunction/`：線性回歸與股價預測

| 檔案 | 說明 |
| --- | --- |
| LinearRegressionDemo1.py ~ 3.py | 以唸書時數預測考試分數為例，示範線性回歸基礎概念 |
| machineLearning.py | 用 yfinance 取得 AAPL 股價，計算 5日/20日移動平均與 RSI 作為特徵，訓練線性回歸模型預測收盤價 |

## 環境需求

Python 3.x，需安裝 `yfinance`、`scikit-learn`、`matplotlib` 等套件。
