import pickle
import os

def get_content_dir(path) -> list[str]:
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def load_tickers(info_dir="../data/ticker_infos/", esg_dir='../data/esg_infos'):
    info_tickers = get_content_dir(info_dir)
    for i in info_tickers:
        fd = open(info_dir + i, "rb")
        info = pickle.load(fd)
        print(info)
        fd.close()


if __name__ == '__main__':
    load_tickers()