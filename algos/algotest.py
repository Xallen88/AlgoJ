import pandas as pd
import datetime as d

def test_algo (datamat):

	ret=datamat.iloc[0].tolist()

	m=min(ret)
	highest=[i for i,j in enumerate(ret) if j==m]
	high=min(highest)

	tradevector=[0 for i in range(len(ret))]
	tradevector[high]=1
	tradedf=pd.DataFrame([tradevector], index=[datamat.index[-1]], columns=datamat.columns.values.tolist())

	return tradedf

def cum_return (datamat):
	loser=10

	for t in datamat.columns.values.tolist():
		ret=datamat.ix[:,t].tolist()
		total=1
		for r in ret:
			total=total*r
		if total < loser:
			loser = total
			loserind=t

	tradevector=[0 for i in range(len(datamat.columns.values.tolist()))]
	tradedf=pd.DataFrame([tradevector], index=[datamat.index[-1]], columns=datamat.columns.values.tolist())
	tradedf.at[datamat.index[-1],loserind]=1

	return tradedf

def equal_weights (datamat):
	n=len(datamat.columns.values.tolist())
	w=1/n
	tradevector=[w for i in range(n)]
	tradedf=pd.DataFrame([tradevector], index=[datamat.index[-1]], columns=datamat.columns.values.tolist())

	return tradedf
