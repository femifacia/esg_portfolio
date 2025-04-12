from Asset import Asset

def equal_weight(tickers):
    return [ 1 / len(tickers)] * len(tickers)

def esg_weighted(tickers : list[Asset]):
    total_sum = sum(i.esg_total_score for i in tickers)
    if total_sum == 0:
        return equal_weight(tickers)
    weights = [i.esg_total_score / total_sum for i in tickers]
    return weights

map_weight ={'Equally weighted' : equal_weight,
                   'ESG Total Score weighted' : esg_weighted}