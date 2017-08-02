import pandas as pd
import datetime as d
import math

trendoutput="trends/test.csv"

def find_trend(datamat, training, freq, algo, subalgo=0):
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
		if subalgo==0:
			trade=algo(datasubset)
		else:
			trade=algo(datasubset, subalgo)
		trademat=trademat.append(trade)

	trademat.to_csv(trendoutput)

def single_compare (datamat, trend):
	ticker=[]
	for t in datamat.columns.values.tolist():
		if trend(datamat[t].tolist()):
			ticker.append(t)
	tradedf=pd.DataFrame([0 for i in range(len(datamat.columns))], index=datamat.columns.values.tolist(), columns=[datamat.index[-1]]).transpose()
	tradedf[ticker]=1
	return tradedf

def big_spike (stockvec, bs=1.03):
	spikes=[i for i in stockvec if i>bs]
	return len(spikes)>0
