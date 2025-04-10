import ticker_utilities

class Portfolio:

    def addUniverse(self, universe):
        self.universe.append(universe)
        self.tickers += ticker_utilities.get_universe_tickers(universe)

    def __init__(self, universe=[]):
        self.universe = []
        self.tickers = []
        self.weights = None
        self.weight_compute_function = None
