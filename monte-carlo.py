import numpy as np
from numpy.random import randn
import time
import yfinance as yf

# pricing an european option
# expiry date, strike price, payoff
# payoff on final day is max(price-strike,0)
# if we get profit we buy otherwise we don't and dont get a loss (other than the price paid for the ticket)
# discount (b) is that value of money decreases with time and for over n period we raise it to power n 
# fair price of option = (discount)^n * (average price of option on expiry date)
# average price of option on expiry date = mean{max(price-strike,0)}



def market_data(ticker_symbol):
    print(f"Downloading 1 year of data for {ticker_symbol}....")
    stock_data = yf.download(ticker_symbol,period="1y")
    prices = stock_data['Close'].squeeze()

    log_returns = np.log(prices/prices.shift(1)).dropna()

    daily_vol = log_returns.std()
    sigma = daily_vol * np.sqrt(252)

    daily_mu = log_returns.mean()
    mu = daily_mu *252 
    
    S0 = float(prices.iloc[-1])
    print("-" * 30)
    print(f"Current Price (S0): ${S0}")
    print(f"Historical Annual Drift (μ): {mu}")
    print(f"Historical Annual Volatility (σ): {sigma}")
    print("-" * 30)
    return S0, mu, sigma
# real parameters now
S0, mu, sigma = market_data("AAPL")
strike_price = S0+10.0
u = mu
v = sigma
days_to_expiry=30
    # taking a random value from normal distribution, then adjusting it using drift and volatality and then converting to lognormal to get rid of negative values
def pricing_european_option(num_simulations=100000):
    T = days_to_expiry/252
    b=0.95

    drift_adjustment = (mu-sigma**2/2)*T
    shock = sigma*np.sqrt(T)*randn(num_simulations)
    final_stock_price = S0*np.exp(drift_adjustment+shock)
    payoff = np.maximum(final_stock_price-strike_price,0) 

    average_payoff = np.mean(payoff)
    option_price = (b**T)*(average_payoff)

    return option_price

start_time = time.time()
price = pricing_european_option()
end_time = time.time()

print(price)
print(end_time-start_time)
