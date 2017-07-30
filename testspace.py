import pandas as pd
import datetime as d
import read_stocks as rs
import analytics as anal

trades = "trades/tradetest.csv"

returnsmat = rs.read_stocks("2017-07-20", "2017-07-28", 0)
trademat = pd.read_csv(trades, index_col=0)

ret = anal.total_return (returnsmat, trademat, "2017-07-28")

print ("{0:f}" .format(ret))
