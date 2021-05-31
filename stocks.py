import yfinance as yf
import streamlit as st

st.write("""
# App Precio de acciones usando la API de Yahoo! Finance
Datos de las acciones de X empresas , mostrando **precio de cierre** y ***volumen***
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol 
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Google (GOOGL) Precio de cierre
""")#El precio de cierre se calcula dividiendo el producto total por el número total de acciones negociadas durante los 30 minutos.


st.line_chart(tickerDf.Close)
st.write("""
## Google (GOOGL) Volumen
""")
st.line_chart(tickerDf.Volume)



#define the ticker symbol 
tickerSymbol = 'YPF'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## YPF (YPF) Precio de cierre
""")#El precio de cierre se calcula dividiendo el producto total por el número total de acciones negociadas durante los 30 minutos.


st.line_chart(tickerDf.Close)
st.write("""
## YPF (YPF) Volumen
""")
st.line_chart(tickerDf.Volume)