import pandas as pd
import datetime as d


def trade_return (returnsmat, ticker, start, end):
	tradereturn = 1

	stockreturn = returnsmat.ix[start:end, ticker].tolist()
	stockreturn.pop(0)

	for ret in stockreturn:
		tradereturn = tradereturn * ret

	return tradereturn

def returns_anal (returnsmat, trademat, end, anal):
	ret = 1
	tradereturn = 0

	tradedates = trademat.index.tolist()

	if d.datetime.strptime(returnsmat.index[-1], "%Y-%m-%d") < d.datetime.strptime(end, "%Y-%m-%d"):
		tradedates.append(returnsmat.index[-1])
	else:
		tradedates.append(end)

	tickers = trademat.columns.values.tolist()
	for td, ntd in zip(tradedates[:-1], tradedates[1:]):
		for stock in tickers:
			if trademat.at[td,stock] != 0:
				tradereturn = trade_return (returnsmat, stock, td, ntd) * trademat.at[td,stock] + tradereturn
		ret=anal(ret,tradereturn) 	# function-dependent
		tradereturn = 0

	return anal(ret, tradereturn, len(tradedates))


def total_return (ret, tradereturn, n=0):
	if n>0:
		return ret
	else:
		return ret*tradereturn

def positive_returns (ret, tradereturn, n=0):
	if n>0:
		return (ret-1)/n
	else:
		if tradereturn>1:
			return ret+1
		else:
			return ret

def big_loss (ret, tradereturn, n=0):
	if n>0:
		return (ret-1)/n
	else:
		bl=0.90
		if tradereturn<bl:
			return ret+1
		else:
			return ret
