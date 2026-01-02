import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Analyzer")
st.write("Analyze historical stock prices and visualize trends.")

col1, col2, col3 = st.columns(3)

with col1:
    company = st.selectbox(
    "Select Company",
    ("MSFT", "AAPL", "GOOG", "AMZN", "TSLA"),
)

with col2:
   sd = st.date_input("Start Date", datetime.date(2024, 1, 1))

with col3:
    ed = st.date_input("End Date", datetime.date(2025, 12, 31))


data=yf.Ticker(company)
ticker_data=data.history(start=sd, end=ed)

st.subheader("Stock Prices for " + company)
st.dataframe(ticker_data.head())

st.subheader("Stock Prices for " + company)
st.line_chart(ticker_data['Close'])
st.subheader("Volume for " + company)
st.bar_chart(ticker_data['Volume'])