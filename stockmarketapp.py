import streamlit as st
import yfinance as yf
import datetime as dt


col1,col2,col3=st.columns(3)
with col1:
    ticker_symbol=st.text_input('Enter the ticker symbol','AAPL')
with col2:
    start_date=st.date_input('From',dt.date(2019,1,7))
with col3:
    end_date=st.date_input('Till',dt.date(2023,1,7))

data=yf.download(ticker_symbol,start=start_date,end=end_date)

st.write(data)
st.line_chart(data['Close'])