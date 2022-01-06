from pandas_datareader.stooq import StooqDailyReader
from datetime import datetime
import matplotlib.pyplot as plt

start = datetime(2021, 1, 1)
end = datetime(2021, 12, 31)
brand = '1321.JP'

stooq = StooqDailyReader(brand, start=start, end=end)
data = stooq.read()  # pandas.core.frame.DataFrame
plt.figure()
data[['Open', 'High', 'Low', 'Close']].plot()
plt.savefig('graph.png')
