import yfinance as yf

class Asset:
    def __init__(self,ticker : str, sector : str, country : str, esg : int):
        self.ticker = ticker
        self.sector = sector
        self.country = country
        self.esg = esg
class Portfolio:
    def __init__(self):
        pass
ticker = yf.Ticker("AAPL")
info = ticker.info
esg = info.get("esgScores", {})
print(ticker.info)