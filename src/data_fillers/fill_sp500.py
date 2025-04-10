import pandas as pd


def sp500_membership_filler(path  : str = '../../data/memberships/'):
    fd = open(path + 'SP500', 'w')
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    sp500_df = tables[0]
    tickers = sp500_df['Symbol'].tolist()
    tickers.sort()
    for i in tickers:
        fd.write(i + '\n')
    fd.close()


if __name__ == '__main__':
    sp500_membership_filler()