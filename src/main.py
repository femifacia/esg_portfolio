import yfinance as yf
from Portfolio import Portfolio
from Asset import Asset
import filters_universe
import weight_portfolio

portfolio = Portfolio()
portfolio.addUniverse('SP500')
#print(portfolio.tickers_arr)
#print('filter')
portfolio.addFilter(filters_universe.get_ten_tickers_random, 1)
#print(portfolio.filtered_tickers_arr)
portfolio.addFilter(filters_universe.get_ten_tickers_random, 0)
#print(portfolio.filtered_tickers_arr)
portfolio.computeWeight(weight_portfolio.equal_weight)
#portfolio.backtest()
portfolio.plotPerf()

#ticker = yf.Ticker("AAPL")
#info = ticker.info
#esg = info.get("esgScores", {})
#print(ticker.info)


#countries_found = None
#sectors_found = None
#exchanges_found = None
#
##@st.cache_data
#def load_criteria_info():
#    global countries_found
#    global sectors_found
#    global exchanges_found
#    tickers = ticker_utilities.load_tickers()
#    print("ah",tickers)
#    countries_found = ticker_utilities.get_countries(tickers)
#    sectors_found = ticker_utilities.get_sector(tickers)
#    print('huuumm', sectors_found)
#    exchanges_found = ticker_utilities.get_exchange(tickers)
#
#load_criteria_info()