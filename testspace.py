import pandas as pd
import datetime as d
import read_stocks as rs
import analytics as anal
import algos.algos as algo
import run_algo as ra
import trends.trends as trend

trades = run_algo.tradeoutput
trends = trend.trendouput

datamat = rs.read_stocks("2016-08-02", "2017-07-28", 0)

trend.find_trend(datamat, 7, 7, trend.single_compare, trend.big_spike)

#trademat = pd.read_csv(trades, index_col=0)

#ret = anal.returns_anal (datamat, trademat, "2017-07-28", anal.total_return)

#print ("{0:f}" .format(ret))
