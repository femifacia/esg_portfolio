class Asset:
    def __init__(self,ticker : str = None, sector : str= None, country : str= None, esg : int= None, exchange : str= None):
        self.ticker = ticker
        self.sector = sector
        self.country = country
        self.esg = esg
        self.exchange = exchange

    def load_info(self, info):
        sah = []
        for i in info:
            sah.append(i)
        sah.sort()
        #[print(i) for i in sah]
#        print(self.ticker)
        if 'exchange' in info:
            self.exchange = info['exchange']
        else:
            self.exchange = 'NA'
        if 'sector' in info:
            self.sector = info['sector']
        else:
            self.sector = 'Consumer Cyclical'
        if 'country' in info:
            self.country = info["country"]
        elif 'region' in info:
            self.country = info['region']
        else:
            self.country = 'NA'
    
    def load_esg(self, esg_data):
        self.esg_data = esg_data