import numpy as np
from numpy.random import randn
import time

# doing it using for loops to test the time

# let's say i have a stock price which depends on three random factors (X1,X2,X3) (like inflation, company sales, interest rate etc)
# i am using monte carlo to simulate it for 100000 times to find the expected value of the stock price
# expected value means mean
# let the difficult equation that tells the stock price to be S = (X1+X2+X3)^p


# the fixed parameters are founded and given by financial researchers
# i am assuming them to be as follows:
p = 0.5
# means
u1 = 0.2
u2 =0.8
u3 = 0.4
# volatality
v1=0.1
v2=0.05
v3=0.2

# as the stock prices cannot be negative so we take the log of the normal distribution and use a variation called lognormal to have only zero and positive values of stocks
def compute_mean(n=100000):
    S = 0.0

    # now we need random values for the three factors
    X1 = np.exp(u1+v1*randn(n))
    X2 = np.exp(u2+v2*randn(n))
    X3 = np.exp(u3+v3*randn(n))
    # now we are getting three arrays of random numbers adjusted using average and volatility
    # Formula: S = (X1 + X2 + X3)^p
    S = (X1+X2+X3)**p # matrices addition and every element is raised to p

    return S.mean()


# timing
start_time = time.time()
expected_value = compute_mean()
end_time = time.time()

print(expected_value)
print(end_time-start_time)


# for loop result
# 2.2294349067883807
# 0.09608006477355957
# 2.229575767062145
# 0.06717205047607422

# vectorization result 
# 2.229568070813988
# 0.004385948181152344
# 2.229989240284386
# 0.004126071929931641