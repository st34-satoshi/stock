from pandas_datareader.stooq import StooqDailyReader
from datetime import datetime

start = datetime(2020, 1, 1)
end = datetime(2020, 2, 1)
brand = '9984.JP'

stooq = StooqDailyReader(brand, start=start, end=end)
data = stooq.read()  # pandas.core.frame.DataFrame
print(data)
