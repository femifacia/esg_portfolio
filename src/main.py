import yfinance as yf
from Portfolio import Portfolio
from Asset import Asset
import filters_universe

portfolio = Portfolio()
portfolio.addUniverse('SP500')
print(portfolio.tickers_arr)
print('filter')
portfolio.addFilter(filters_universe.get_ten_tickers_random, 1)
print(portfolio.filtered_tickers_arr)
portfolio.addFilter(filters_universe.get_ten_tickers_random, 0)
print(portfolio.filtered_tickers_arr)

#ticker = yf.Ticker("AAPL")
#info = ticker.info
#esg = info.get("esgScores", {})
#print(ticker.info)