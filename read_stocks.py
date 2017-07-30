import pandas as pd
import datetime as d

database = "data/datatest.csv"

def read_stocks(s, e, opt):
    """
    This function reads in the data from a CSV file 
    with the restrictions specified
    
    :param s: Start of data
    :param e: End of data
    :param opt: Options for reading
    :return: Dataframe of stock data
    """

    stocks = pd.read_csv(database, index_col=0)

    # Trim stocks before start date & after end date
    if s > stocks.index[0]:
        while True:
            try:
                start = stocks.index.get_loc(s)
                break
            except KeyError:
                s_temp = d.datetime.strptime(s, "%Y-%m-%d") + d.timedelta(days=1)
                s = d.datetime.strftime(s_temp, "%Y-%m-%d")
        stocks.drop(stocks.head(start).index, inplace=True)

    if e < stocks.index[-1]:
        while True:
            try:
                end = stocks.index.get_loc(e)
                break
            except KeyError:
                e_temp = d.datetime.strptime(e, "%Y-%m-%d") - d.timedelta(days=1)
                e = d.datetime.strftime(e_temp, "%Y-%m-%d")
        stocks.drop(stocks.index[end+1:], inplace=True)

    # Remove columns according to opt criteria (penny stocks on/off)
    # if opt == "p":
    #     pass
    # elif opt == "d":
    #     pass
    # else:
    #     pass

    return stocks
