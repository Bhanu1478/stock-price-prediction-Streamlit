import streamlit as st
from datetime import date
import yfinance
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START ="2015-01-01"
TODAY =date.today().strftime("Y-%m-%d")

st.title("Stock prediction app")

stocks =("GOOG","AAPL","MSFT","GME")
selected_stock =st.selectbox("Select stock",stocks)