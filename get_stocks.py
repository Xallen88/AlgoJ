import pandas as pd
import pandas_datareader as pdr
from pandas_datareader._utils import RemoteDataError
import datetime as d

database = "datatest.csv"
tickerlist = "tickerstest.txt"

# Takes in ticker list and returns stock data
def stock_reader(ticker, st, e):
    """
    Get stock data from Yahoo Finance
    
    :param ticker: List of stock symbols
    :param st: Start date
    :param e: End date
    :return: List of stock dataframes
    """

    i = 0
    err = []
    ret = []
    for t in ticker:
        try:
            ret.append(pdr.DataReader(t, "yahoo", st, e))
        except RemoteDataError:
            try:
                ret.append(pdr.DataReader(t + "X", "yahoo", st, e))
                ticker[i] = t + "X"
            except RemoteDataError:
                err.append(i)
        i += 1
    for j in reversed(err):
        ticker.pop(j)
    return ret


# Turns a list & index into a data frame
def mk_dataframe(listy, ind):
    """
    Converts list to dataframe
    
    :param listy: List of dataframes
    :param ind: Index list
    :return: Dataframe
    """

    stocklist = []
    for li in listy:
        try:
            stocklist.append(li["Adj Close"])
        except TypeError:
            pass
    stockmatrix = pd.DataFrame(stocklist)
    stockmatrix.index = ind
    stockmatrix = stockmatrix.transpose()

    # Remove stat holidays from data
    null_list = []
    for j in range(len(stockmatrix)):
        if stockmatrix.at[stockmatrix.index[j], "AAPL"] == "NaN":
            null_list.append(j)
    stockmatrix.drop(stockmatrix.index[null_list], inplace=True)

    return stockmatrix

# Start/End dates for stock data
years = 1
end = d.date.today()
start = end - d.timedelta(days=10)

# Ticker List
tickers = []
with open(tickerlist) as file:
    for line in file:
        tickers.append(line.rstrip("\n"))

stocks = stock_reader(tickers, start, end)

stockmat = mk_dataframe(stocks, tickers)

# Ouput new ticker list
file_out = open("tickers_new.txt", "w")
for t in tickers:
    file_out.write("{}\n" .format(t))
file_out.close()

# Store in CSV
stockmat.to_csv(database)
