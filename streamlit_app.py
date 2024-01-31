import streamlit as st
import yfinance as yf


def main():
    st.title("Finance Explorer")

    # Get user input for stock symbol
    stock_symbol = st.text_input("Enter stock symbol (e.g., AAPL):")

    # Fetch stock data based on user input
    if stock_symbol:
        stock_data = fetch_stock_data(stock_symbol)
        if stock_data is not None:
            st.write("### Stock Data")
            st.write(stock_data)
        else:
            st.write("Stock data not found. Please enter a valid stock symbol.")


def fetch_stock_data(symbol):
    """
    Function to fetch stock data from Yahoo Finance based on the given symbol.
    """
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1mo")  # Fetching data for the past month
        return data
    except:
        return None


if __name__ == "__main__":
    main()
