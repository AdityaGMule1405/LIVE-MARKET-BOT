import yfinance as yf
from datetime import datetime, timedelta

def get_live_data():
    today = datetime.now()
    past_15_days = today - timedelta(days=15)
    tickers = ['ICICIBANK.NS', 'TATAPOWER.NS']
    data = {}
    for ticker in tickers:
        try:
            # Download data for the last 15 days, adjust period as needed to ensure enough data for 15 closing prices
            # Using 20 days to be safe for 15 closing prices, as some days might be holidays/weekends
            df = yf.download(ticker, start=past_15_days.strftime('%Y-%m-%d'), end=today.strftime('%Y-%m-%d'))
            if not df.empty:
                # Get the last 15 closing prices, if available
                closing_prices = df['Close'].tail(15).tolist()
                data[ticker] = closing_prices
            else:
                data[ticker] = [] # No data found
        except Exception as e:
            print(f'Error fetching data for {ticker}: {e}')
            data[ticker] = []
    return data
