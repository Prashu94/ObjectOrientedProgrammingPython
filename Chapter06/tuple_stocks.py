import datetime
from collections import namedtuple

# tuples
def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low)/2), date)

mid_value, date = middle(("FB", 177.46, 178.67, 175.79), datetime.date(2021, 12, 26))

print(mid_value, date)

Stock = namedtuple("Stock", ["symbol", "current", "high", "low"])
stock = Stock("FB", 177.146, high=178.67, low=175.79)
print(stock)