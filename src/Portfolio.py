import ticker_utilities
import yfinance as yf
import pandas as pd
import filters_universe


class Portfolio:

    def plotPerf(self):
        data = yf.download(self.bench, start=self.start)['Close']
        self.bench_df = data
        print(data)
        pass

    def backtest(self):
        tickers = [i.ticker for  i in self.filtered_tickers_arr]
        print(self.weights)
        data = yf.download(tickers, start=self.start, end=self.end)['Close']
        data = data.ffill()
        data = data.bfill()
        data['portfolio'] = data.multiply(self.weights, axis=1).sum(axis=1)
        #data.fillna(0)
        print(data)
        self.df = data


    def computeWeight(self, func_weight):
        self.weights = func_weight(self.filtered_tickers_arr)

    def cut_out_of_cart_tickers(self, nbr : int):
        self.filtered_tickers_arr = self.filtered_tickers_arr[:nbr]
        self.filtered_tickers_set = set(self.filtered_tickers_arr)

    def addFilterWithArgsFromKey(self, filter_func_name, args, is_and = 1):
#        cmp = self.filtered_tickers_set if is_and else self.tickers_set
        if self.filter_count == 0:
            is_and = 0
        filter_func = filters_universe.map_filters[filter_func_name]
        tickers_found = set(filter_func(self.tickers_arr, **args))
        if is_and:
            self.filtered_tickers_set &= tickers_found
        else:
            self.filtered_tickers_set |= tickers_found
        self.filtered_tickers_arr = list(self.filtered_tickers_set)
        self.filter_count += 1

    def addFilterWithoutArgs(self, filter_func, is_and = 1):
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

    def __init__(self, universe=[], start='2018-01-01', end='2025-01-01'):
        self.universe = []
        self.tickers_arr = []
        self.tickers_set = set()
        self.weights = None
        self.weight_compute_function = None
        self.filtered_tickers_arr = []
        self.filtered_tickers_set = set()
        self.filter_count = 0
        self.start = start
        self.end = end
        self.bench = ['SUSW.L']

        for i in universe:
            self.addUniverse(i)
