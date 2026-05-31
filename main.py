import pandas as pd
from live_fetcher import get_live_data
from indicators import calculate_rsi

def main():
    print('Fetching live data...')
    live_data = get_live_data()
    
    if not live_data:
        print('No live data fetched. Exiting.')
        return

    report_data = []
    for ticker, prices in live_data.items():
        if prices:
            rsi = calculate_rsi(prices)
            report_data.append({"Ticker": ticker, "RSI": rsi})
            print(f'Ticker: {ticker}, RSI: {rsi}')
        else:
            report_data.append({"Ticker": ticker, "RSI": "N/A"})
            print(f'No sufficient data for {ticker} to calculate RSI.')

    if report_data:
        df_report = pd.DataFrame(report_data)
        df_report.to_csv('live_report.csv', index=False)
        print('Live report saved to live_report.csv')
    else:
        print('No data to report.')

if __name__ == '__main__':
    main()
