import streamlit as st
import pandas as pd
import numpy as np
import ticker_utilities
from Portfolio import Portfolio


@st.cache_resource
def init_portfolio():
    return [None]

@st.cache_resource
def get_portfolio(universe : list[str], filters : dict[str], weights : str, sort_cri, start : str, end : str, nbr_tickers : int, is_rand=0):
    portf = Portfolio(universe, start=start, end=end)
    for i in filters:
        portf.addFilterWithArgsFromKey(i, filters[i])
    portf.addSortCriteria(sort_cri)
    if len(portf.filtered_tickers_arr) == 0:
        return ["na"]
    portf.cut_out_of_cart_tickers(nbr_tickers)
    portf.computeWeightFromKey(weights)
    print(portf.filtered_tickers_arr)
    for i in (portf.filtered_tickers_arr):
        i.describe()
    print(portf.weights)
    #portf.backtest()
    return portf


portfolio = init_portfolio()
@st.cache_resource
def init_generating_error(is_error : bool) -> list[bool]:
    return [0]

@st.cache_resource
def init_error_message(mess : str) -> list[str]:
    return [""]

@st.cache_resource
def get_random_portfolio_bool():
    return [0]

is_rand_portfolio = get_random_portfolio_bool()

countries_found = None
sectors_found = None
exchanges_found = None
is_generating_error = init_generating_error(0)
error_message = init_error_message("")

@st.cache_data
def load_criteria_info():
    tickers = ticker_utilities.load_tickers()
    print("ah",tickers)
    countries_found = ticker_utilities.get_countries(tickers)
    sectors_found = ticker_utilities.get_sector(tickers)
    print('huuumm', sectors_found)
    exchanges_found = ticker_utilities.get_exchange(tickers)
    return countries_found, sectors_found, exchanges_found

countries_found, sectors_found, exchanges_found = load_criteria_info()

sort_esg_criteria_arr =  ['ESG Total note ascending',
                          "ESG Total note descending",
                          'Ascending lexicographic order on ticker names',
                          'Descending lexicographic order on ticker names',
                          'Random',
                          'None'
                          ]


weight_criteria = ['Equally weighted',
                   'ESG Total Score weighted']

st.title('Portolio ESG Builder')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

data_load_state = st.text("Let's build an ESG Portfolio")
st.sidebar.title("Criteria & Filters")
st.sidebar.subheader("Universe Picking")
universe_input = st.sidebar.multiselect("Universe", ["SP500"], 'SP500')

st.sidebar.subheader("Filters")
#print(sectors_found)
sectors_accepted = st.sidebar.multiselect("Sectors Accepted", sectors_found)
countries_accepted = st.sidebar.multiselect("Countries Accepted", countries_found)
exchanges_accepted = st.sidebar.multiselect("Exchange Accepted", exchanges_found)
min_esg_total_note = st.sidebar.slider('Minimum ESG Total Score', 0, 100, 0)
max_esg_total_note = st.sidebar.slider('Maximum ESG Total Score', 1, 101, 101)

st.sidebar.subheader("Weight for tickers")
weight_input = st.sidebar.radio("Weights", weight_criteria)



st.sidebar.subheader("Sort criteria")
sort_input= st.sidebar.radio("Sort by", sort_esg_criteria_arr)

st.sidebar.subheader("Max numbers of tickers")
nbr_tickers_input = st.sidebar.slider('Number of tickers', 1, 39, 5)
nbr_ticker = st.slider('Tickers', 1, 50, 17)

st.sidebar.subheader("Date Range")
start_date_input = st.sidebar.date_input("Start Date", "2018-01-01")
end_date_input = st.sidebar.date_input("Stop Date")

#print(start_date_input)
st.sidebar.subheader("Generation")

def generate_portfolio_onclick(*args, **kwargs):
    global is_generating_error
    global error_message
    universe = universe_input
    if len(universe) == 0:
        is_generating_error[0] = 1
        error_message[0] = 'Empty Universe. Choose your universes'
        return
    if min_esg_total_note >= max_esg_total_note:
        is_generating_error[0] = 1
        error_message[0] = 'Minimum Total ESG Score Has to be **Lower than** Maximum Total ESG Score'
        return
    is_generating_error[0] = 0
    error_message[0] = 0
    universe = universe_input
    filters  = {
        "sectors_accepted" : {'sectors_accepted':sectors_accepted},
        "countries_accepted" : {'countries_accepted' : countries_accepted},
        "exchange_accepeted" : {'exchange_accepted' : exchanges_accepted},
        "min_esg_total_note" : {'min_esg_total_note' : min_esg_total_note},
        "max_esg_total_note" : {"max_esg_total_note" : max_esg_total_note}


    }
    weights = weight_input
    sort_cri = sort_input
    start = start_date_input
    end = end_date_input
    nbr_tickers  = nbr_tickers_input
    portfolio[0] = get_portfolio(universe=universe,filters=filters,weights=weights,sort_cri=sort_cri,start=start,end=end,nbr_tickers=nbr_tickers, is_rand=is_rand_portfolio[0])
    if sort_cri == 'Random':
        is_rand_portfolio[0] = is_rand_portfolio[0] + 1



 
generate_input = st.sidebar.button('Generate Portfolio',on_click=generate_portfolio_onclick)

if is_generating_error[0]:
    print('kkk')
    st.sidebar.error(error_message[0])




@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

if portfolio[0] is None:
    st.text("Let's Build a portfolio")
    st.image("../img/Finance app-pana.png")
elif portfolio[0] == 'na':
    st.text('No ticker found!!!')
    st.text('Please reset your filters!')
    st.image("../img/Empty-pana.png")

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)