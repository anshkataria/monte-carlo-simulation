import numpy as np
from numpy.random import randn
import time

# pricing an european option
# expiry date, strike price, payoff
# payoff on final day is max(price-strike,0)
# if we get profit we buy otherwise we don't and dont get a loss (other than the price paid for the ticket)
# discount (b) is that value of money decreases with time and for over n period we raise it to power n 
# fair price of option = (discount)^n * (average price of option on expiry date)
# average price of option on expiry date = mean{max(price-strike,0)}


# let us define the parameters now

n = 10 # expiry period
b = 0.95 # discount
strike_price = 1.0
u = 1.0
v = 0.1
        # taking a random value from normal distribution, then adjusting it using drift and volatality and then converting to lognormal to get rid of negative values
def pricing_european_option(num_simulations=100000):

    final_stock_price = np.exp(u+v*np.random.randn(num_simulations))
    payoff = np.maximum(final_stock_price-strike_price,0) 

    average_payoff = np.mean(payoff)
    option_price = (b**n)*(average_payoff)

    return option_price

start_time = time.time()
price = pricing_european_option()
end_time = time.time()

print(price)
print(end_time-start_time)
