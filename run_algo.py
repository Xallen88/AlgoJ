import pandas as pd
import datetime as d
import math

tradeoutput="trades/test1.csv"

def run_algo(datamat, algo, training):
	"""
	Runs an algorithm and outputs a trade matrix

	:param datamat: Dataframe containing stock returns
	:param algo: Algorithm function
	:param training: Length of time to use for training
	"""

	end=d.datetime.strptime(datamat.index[0],"%Y-%m-%d")
	trademat=pd.DataFrame(columns=datamat.columns.values.tolist())

	runs=math.ceil(len(datamat.index)/training)-1
	for i in range(runs):
		start=end
		end=end+d.timedelta(days=training)
		while(True):
			if d.datetime.strftime(end,"%Y-%m-%d") in datamat.index:
				break
			else:
				end=end+d.timedelta(days=1)

		datasubset=datamat.ix[d.datetime.strftime(start,"%Y-%m-%d"):d.datetime.strftime(end,"%Y-%m-%d")]
		trade=algo(datasubset)
		trademat=trademat.append(trade)

	trademat.to_csv(tradeoutput)
