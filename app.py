import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

st.title("📈 Mujahidul's Trading Dashboard")

symbol = st.text_input("Enter Stock Symbol", "AAPL")
data = yf.download(symbol, period="30d")

fig = go.Figure(data=[go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close']
)])
st.plotly_chart(fig, use_container_width=True)
