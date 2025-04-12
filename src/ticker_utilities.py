import pickle
import os
import Asset

def get_universe_tickers(universe_name : str, membership_dir = './data/memberships/',info_dir = './data/ticker_infos/', esg_dir='./data/ticker_esg/'):
    ans  = []
    
    fd = open(membership_dir + universe_name)
    universe_ticker_name = list(filter(lambda x : x, fd.read().split('\n')))
    fd.close()

    for i in universe_ticker_name:
        fd = open(info_dir + i, 'rb')
        info = pickle.load(fd)
        fd.close()
        asset = Asset.Asset(i)
        asset.load_info(info)
        fd = open(esg_dir + i, 'rb')
        esg_data = pickle.load(fd)
        fd.close()
        asset.load_esg(esg_data)
        ans.append(asset)

    return  ans

def get_content_dir(path) -> list[str]:
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def load_tickers(info_dir="./data/ticker_infos/", esg_dir='./data/ticker_esg/'):
    info_tickers = get_content_dir(info_dir)
    info_tickers.sort()
    ans = []
#    print(info_tickers)
    for i in info_tickers:
        fd = open(info_dir + i, "rb")
        info = pickle.load(fd)
        asset = Asset.Asset(i)
        asset.load_info(info)
#        print(info)
        fd.close()
#        print(i)
        fd = open(esg_dir + i, 'rb')
        esg_data = pickle.load(fd)
#        print(esg_data)
        fd.close()

        asset.load_esg(esg_data)
        ans.append(asset)
    return ans

def get_countries(tickers : list[Asset.Asset]) -> set[str]:
    print("AH")
    ans = set()
    for i in tickers:
        ans.add(i.country)
    return ans


def get_sector(tickers : list[Asset.Asset]) -> set[str]:
    ans = set()
    for i in tickers:
        ans.add(i.sector)
    return ans

def get_exchange(tickers : list[Asset.Asset]) -> set[str]:
    ans = set()
    for i in tickers:
        ans.add(i.exchange)
    return ans


if __name__ == '__main__':
    load_tickers()