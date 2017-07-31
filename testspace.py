import pandas as pd
import datetime as d
import read_stocks as rs
import analytics as anal
import algos.algotest as algo
import run_algo as ra

trades = "trades/test1.csv"

datamat = rs.read_stocks("2016-08-02", "2017-07-28", 0)

ra.run_algo(datamat, algo.test_algo, 7)

trademat = pd.read_csv(trades, index_col=0)

ret = anal.total_return (datamat, trademat, "2017-07-28")

#print (datamat.[0])
print ("{0:f}" .format(ret))
