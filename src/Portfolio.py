import ticker_utilities



class Portfolio:

    def addFilter(self, filter_func, is_and = 0):
#        cmp = self.filtered_tickers_set if is_and else self.tickers_set
        if self.filter_count == 0:
            is_and = 0
        tickers_found = set(filter_func(self.tickers_arr))
        if is_and:
            self.filtered_tickers_set &= tickers_found
        else:
            self.filtered_tickers_set |= tickers_found
        self.filtered_tickers_arr = list(self.filtered_tickers_set)
        self.filter_count += 1


    def addUniverse(self, universe):
        self.universe.append(universe)
        new_tickers = ticker_utilities.get_universe_tickers(universe)
        self.tickers_arr += new_tickers
        self.tickers_set |= set(new_tickers)

    def __init__(self, universe=[]):
        self.universe = []
        self.tickers_arr = []
        self.tickers_set = set()
        self.weights = None
        self.weight_compute_function = None
        self.filtered_tickers_arr = []
        self.filtered_tickers_set = set()
        self.filter_count = 0
