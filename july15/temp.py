#| echo: false
#| fig-cap: "iShares Japan JGB ETF (IGIB) Price - Last 20 Years"

import yfinance as yf
import matplotlib.pyplot as plt

try:
    # Fetch data for the iShares Japan 7-10 Year JGB ETF (IGIB) as a proxy
    jgb_etf = yf.Ticker("IGIB")
    hist = jgb_etf.history(period="20y")

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(hist.index, hist['Close'], color='#D9534F', linewidth=2)

    # Style the plot
    ax.set_title('iShares Japan JGB ETF (IGIB) Price', fontsize=14)
    ax.set_ylabel('Price (JPY)')
    ax.grid(True, linestyle='--', alpha=0.6)
    fig.autofmt_xdate()
    
    plt.show()

except Exception as e:
    print(f"<p style='color: red;'>Could not load JGB ETF chart. Error: {e}</p>")
