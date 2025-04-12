from random import shuffle
from Asset import Asset





def get_sectors_accepted(tickers : list[Asset], sectors_accepted : list[str]):
    if len(sectors_accepted) == 0:
         return tickers
    sectors_accepted = set(sectors_accepted)
    ans = []
    for i in tickers:
         if i.sector in sectors_accepted:
              ans.append(i)
    return ans

def get_countries_accepted(tickers : list[Asset], countries_accepted : list[str]):
    if len(countries_accepted) == 0:
         return tickers
    accepted = set(countries_accepted)
    ans = []
    for i in tickers:
         if i.country in accepted:
              ans.append(i)
    return ans

def get_exchange_accepted(tickers : list[Asset], exchange_accepted : list[str]):
    if len(exchange_accepted) == 0:
         return tickers
    accepted = set(exchange_accepted)
    ans = []
    for i in tickers:
         if i.exchange in accepted:
              ans.append(i)
    return ans

def get_min_esg_total_note(tickers : list[Asset], min_esg_total_note : int):
    ans = []
    for i in tickers:
          if i.esg_total_score >= min_esg_total_note:
               ans.append(i)
    return ans

def get_max_esg_total_note(tickers : list[Asset], max_esg_total_note : int):
    ans = []
    for i in tickers:
          if i.esg_total_score <= max_esg_total_note:
               ans.append(i)
    return ans
     

def get_ten_tickers_random(tickers):
    copy = tickers.copy()
    shuffle(copy)
    return copy[:10]


map_filters = {"sectors_accepted" : get_sectors_accepted,
        "countries_accepted" : get_countries_accepted,
        "exchange_accepeted" : get_exchange_accepted,
        "min_esg_total_note" : get_min_esg_total_note,
        "max_esg_total_note" : get_max_esg_total_note
}

def get_total_note_asc(tickers : list[Asset]):
    ans = sorted(tickers, key =lambda x : x.esg_total_score,reverse=0)
    return ans

def get_total_note_desc(tickers : list[Asset]):
    ans = sorted(tickers, key = lambda x : x.esg_total_score,reverse=1)
    return ans

def get_lexciographical_ticker_asc(tickers : list[Asset]):
    ans = sorted(tickers, key = lambda x : x.ticker,reverse=0)
    return ans


def get_lexciographical_ticker_desc(tickers : list[Asset]):
    ans = sorted(tickers, key = lambda x : x.ticker,reverse=1)
#    print(ans)
#    print("before", tickers)
    return ans


def get_random(tickers : list[Asset]):
    ans = tickers.copy()
    shuffle(ans)
    return ans

def get_no_sort_criteria(tickers : list[Asset]):
    return tickers

map_sort = {'ESG Total note ascending' : get_total_note_asc,
                          "ESG Total note descending" : get_total_note_desc,
                          'Ascending lexicographic order on ticker names' : get_lexciographical_ticker_asc,
                          'Descending lexicographic order on ticker names' : get_lexciographical_ticker_desc,
                          'Random' : get_random,
                          'None' : get_no_sort_criteria
                          }