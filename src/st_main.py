import streamlit as st
import pandas as pd
import numpy as np

st.title('Portolio ESG Builder')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

data_load_state = st.text("Let's build an ESG Portfolio")
nbr_tickers_input = st.sidebar.slider('Tickers', 1, 39, 5)
nbr_ticker = st.slider('Tickers', 1, 50, 17)
def test_onclick(*args, **kwargs):
    if int(nbr_tickers_input) < 10:
        st.sidebar.success("Good")
    else:
        st.sidebar.error("too high")
    
generate_input = st.sidebar.button('Generate Portfolio',on_click=test_onclick)



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

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)