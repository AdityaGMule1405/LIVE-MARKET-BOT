def calculate_rsi(prices, period=14):
    deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    rs_values = []
    rsi_values = []

    for i in range(period, len(gains)):
        if avg_loss == 0:
            rs = 99999 # Handle division by zero, essentially infinite RS
        else:
            rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        rs_values.append(rs)
        rsi_values.append(rsi)

        new_gain = gains[i]
        new_loss = losses[i]

        avg_gain = ((avg_gain * (period - 1)) + new_gain) / period
        avg_loss = ((avg_loss * (period - 1)) + new_loss) / period

    return rsi_values
