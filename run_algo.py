import pandas as pd
import datetime as d
import math

tradeoutput="trades/test1.csv"

def run_algo(datamat, algo, training, freq):
	"""
	Runs an algorithm and outputs a trade matrix

	:param datamat: Dataframe containing stock returns
	:param algo: Algorithm function
	:param training: Length of training set in days
	:param freq: Trading frequency in days
	"""

	start=d.datetime.strptime(datamat.index[0],"%Y-%m-%d")-d.timedelta(days=freq)
	trademat=pd.DataFrame(columns=datamat.columns.values.tolist())
	numdays=d.datetime.strptime(datamat.index[-1],"%Y-%m-%d")-d.datetime.strptime(datamat.index[0],"%Y-%m-%d")

	runs=math.ceil((numdays.days-training)/freq)
	for i in range(runs):
		start=start+d.timedelta(days=freq)
		while(True):
			if d.datetime.strftime(start,"%Y-%m-%d") in datamat.index:
				break
			else:
				start=start+d.timedelta(days=1)
		end=start+d.timedelta(days=training)
		while(True):
			if d.datetime.strftime(end,"%Y-%m-%d") in datamat.index:
				break
			else:
				end=end+d.timedelta(days=1)

		datasubset=datamat.ix[d.datetime.strftime(start,"%Y-%m-%d"):d.datetime.strftime(end,"%Y-%m-%d")]
		trade=algo(datasubset)
		trademat=trademat.append(trade)

	trademat.to_csv(tradeoutput)
