class Asset:
    def __init__(self,ticker : str, sector : str, country : str, esg : int):
        self.ticker = ticker
        self.sector = sector
        self.country = country
        self.esg = esg