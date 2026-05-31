import yfinance as yf
from datetime import datetime, timedelta

def get_live_data():
    today = datetime.now()
    past_15_days = today - timedelta(days=15)
    tickers = ['ICICIBANK.NS', 'TATAPOWER.NS']
    data = yf.download(tickers, start=past_15_days, end=today)
    closing_prices = {}
    for ticker in tickers:
        closing_prices[ticker] = data['Close'][ticker].tolist()
    return closing_prices
