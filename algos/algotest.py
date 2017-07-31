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
