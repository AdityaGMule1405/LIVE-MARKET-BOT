import csv
from live_fetcher import get_live_data
from indicators import calculate_rsi

def main():
    live_data = get_live_data()

    with open('live_report.csv', 'w', newline='') as csvfile:
        fieldnames = ['Ticker', 'Last 15 Days Closing Prices', 'RSI (14-day)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for ticker, prices in live_data.items():
            if len(prices) >= 14:
                rsi_values = calculate_rsi(prices)
                if rsi_values:
                    latest_rsi = rsi_values[-1]
                else:
                    latest_rsi = 'N/A'
            else:
                latest_rsi = 'Not enough data for RSI'
            
            writer.writerow({
                'Ticker': ticker,
                'Last 15 Days Closing Prices': str(prices),
                'RSI (14-day)': latest_rsi
            })

if __name__ == '__main__':
    main()
