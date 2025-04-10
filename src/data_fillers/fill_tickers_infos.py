import yfinance as yf
import tqdm as tqdm
import pickle

def save_info_ticker(path, info, symbol : str):
    fd = open(path + symbol, 'wb')
    pickle.dump(info, fd)
    fd.close


def fill_tickers_info(path_to_membership : str = '../../data/memberships/sp500.txt', dest="../../data/ticker_infos/"):
    tickers = open(path_to_membership).read().split('\n')
    tickers = list(filter(lambda x : x, tickers))
    print(tickers)
    for i in tqdm.tqdm(tickers):
        ticker = yf.Ticker(i)
        info = ticker.info
        save_info_ticker(dest, info, i)


if __name__ == '__main__':
    fill_tickers_info()