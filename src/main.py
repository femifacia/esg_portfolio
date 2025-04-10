import yfinance as yf
from Portfolio import Portfolio
from Asset import Asset

portfolio = Portfolio()
portfolio.addUniverse('SP500')
print(portfolio.tickers[47].sector)

#ticker = yf.Ticker("AAPL")
#info = ticker.info
#esg = info.get("esgScores", {})
#print(ticker.info)