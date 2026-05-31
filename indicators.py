def calculate_rsi(prices, period=14):
    if len(prices) < period + 1:
        return None

    gains = []
    losses = []

    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    avg_gain = sum(gains[0:period]) / period
    avg_loss = sum(losses[0:period]) / period

    rs_values = []
    rsi_values = []

    # Calculate initial RS and RSI
    if avg_loss == 0:
        rs = 1000000 # A very large number to represent infinity
    else:
        rs = avg_gain / avg_loss

    rs_values.append(rs)
    rsi_values.append(100 - (100 / (1 + rs)))

    # Calculate subsequent RS and RSI
    for i in range(period, len(prices)):
        avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
        avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period

        if avg_loss == 0:
            rs = 1000000
        else:
            rs = avg_gain / avg_loss

        rs_values.append(rs)
        rsi_values.append(100 - (100 / (1 + rs)))

    return rsi_values[-1] if rsi_values else None
