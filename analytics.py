import pandas as pd
import datetime as d


def trade_return (returnsmat, ticker, start, end):
	"""
	Return for a single trade of a single ticker

	:param returnsmat: Dataframe of stock returns
	:param ticker: Stock symbol
	:param start: Date of trade (end of day)
	:param end: Date of trade (end of day)
	:return: Return from single trade
	"""

	tradereturn = 1

	stockreturn = returnsmat.ix[start:end, ticker].tolist()
	stockreturn.pop(0)

	for ret in stockreturn:
		tradereturn = tradereturn * ret

	return tradereturn


def total_return (returnsmat, trademat, end):
	"""
	Generates the total return for a given trade matrix

	:param returnsmat: Dataframe of stock returns
	:param trademat: Dataframe of trades (weightings)
	:param end: End of return period
	:return: Total return from trades
	"""

	totalreturn = 1
	tradereturn = 0

	tradedates = trademat.index.tolist()

	if d.datetime.strptime(returnsmat.index[-1], "%Y-%m-%d") < d.datetime.strptime(end, "%Y-%m-%d"):
		tradedates.append(returnsmat.index[-1])
	else:
		tradedates.append(end)

	tickers = trademat.columns.values.tolist()
	for td, ntd in zip(tradedates[:-1], tradedates[1:]):
		for stock in tickers:
			if trademat.at[td,stock] > 0:
				tradereturn = trade_return (returnsmat, stock, td, ntd) * trademat.at[td,stock] + tradereturn
		totalreturn = totalreturn * tradereturn
		tradereturn = 0

	return totalreturn
