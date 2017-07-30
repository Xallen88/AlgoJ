import pandas as pd
import datetime as d
import get_stocks

database = get_stocks.database
tickerlist = get_stocks.tickerlist

# Find last data date
stocks_db = pd.read_csv(database, index_col=0)
start = d.datetime.strptime(stocks_db.index[-1], "%Y-%m-%d") + d.timedelta(days=1)
end = d.date.today()

if start == end:
    quit()    # exit

# Ticker List
tickers = []
with open(tickerlist) as file:
    for line in file:
        tickers.append(line.rstrip("\n"))

# Get stock data
stocks = get_stocks.stock_reader(tickers, start, end)
stockmat = get_stocks.mk_dataframe(stocks, tickers)

# Append csv file with new dataframe
stockmat.to_csv(database, mode="a", header=False)
