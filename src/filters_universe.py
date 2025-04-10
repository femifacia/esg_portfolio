from random import shuffle
from Asset import Asset


def get_ten_tickers_random(tickers):
    copy = tickers.copy()
    shuffle(copy)
    return copy[:10]