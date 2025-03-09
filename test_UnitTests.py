import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import yfinance as yf
import pandas as pd

import week6hw


def test_get_returns():
    # Unit Tests for get_returns
    x = np.array([100, 120, 150, 200])
    rets1 = week6hw.get_returns(x)
    
    assert np.round(rets1[0], 2) == 0.20
    assert np.round(rets1[1], 2) == 0.25
    assert np.round(rets1[2], 2) == 0.33
    
    # Test with real stock data as per professor's instructions
    # F (Ford) from June 1, 2017 to November 30, 2022
    f_prices = week6hw.get_stock_data('F', start="2017-06-01", end="2022-11-30")
    f_returns = week6hw.get_returns(f_prices.values)
    assert len(f_returns) > 0, "Should return non-empty array of Ford returns"
    
    # META from March 6, 2022 to April 3, 2024
    meta_prices = week6hw.get_stock_data('META', start="2022-03-06", end="2024-04-03")
    meta_returns = week6hw.get_returns(meta_prices.values)
    assert len(meta_returns) > 0, "Should return non-empty array of META returns"


# Function to calculate Percent VaR
def test_percent_var():
    # Original unit test
    r = np.random.normal(0.05, 0.03, 1000000)
    # Probability under normal curve within 2 standard deviations
    probability2SD = norm.cdf(2)

    myalpha = probability2SD
    my_percent_var = week6hw.percent_var(r, myalpha)

    assert np.round(my_percent_var, 2) == 0.01
    
    # Test with real stock data as per professor's instructions
    # F (Ford) from June 1, 2017 to November 30, 2022
    f_prices = week6hw.get_stock_data('F', start="2017-06-01", end="2022-11-30")
    f_returns = week6hw.get_returns(f_prices.values)
    f_var = week6hw.percent_var(f_returns, 0.95)
    assert f_var < 0, "VaR for Ford should be negative"
    
    # META from March 6, 2022 to April 3, 2024
    meta_prices = week6hw.get_stock_data('META', start="2022-03-06", end="2024-04-03")
    meta_returns = week6hw.get_returns(meta_prices.values)
    meta_var = week6hw.percent_var(meta_returns, 0.95)
    assert meta_var < 0, "VaR for META should be negative"


def test_es():
    # Unit test with random data
    u = np.random.uniform(0, 100, 100000)
    # Test with alpha = 0.8 (meaning we're focusing on the worst 20% of losses)
    # For a uniform distribution from 0-100, the worst 20% are between 80-100,
    # and their mean is 90
    assert np.round(week6hw.es(losses=u, alpha=0.8), 0) == 90
    
    # Test with a specified VaR of 80 (focusing on losses > 80)
    # For a uniform distribution from 0-100, losses > 80 have a mean of 90
    assert np.round(week6hw.es(losses=u, VaR=80), 0) == 90
    
    # Test with real stock data as per professor's instructions
    # F (Ford) from June 1, 2017 to November 30, 2022
    f_prices = week6hw.get_stock_data('F', start="2017-06-01", end="2022-11-30")
    f_returns = week6hw.get_returns(f_prices.values)
    # Convert negative returns to positive losses and scale by 100 (as in professor's code)
    f_losses = -f_returns[f_returns < 0] * 100
    f_var = week6hw.percent_var(f_returns, 0.95) * -100  # Convert to positive
    f_es = week6hw.es(losses=f_losses, alpha=0.95)
    assert f_es > f_var, "ES should be larger than VaR for Ford"
    
    # META from March 6, 2022 to April 3, 2024
    meta_prices = week6hw.get_stock_data('META', start="2022-03-06", end="2024-04-03")
    meta_returns = week6hw.get_returns(meta_prices.values)
    # Convert negative returns to positive losses and scale by 100 (as in professor's code)
    meta_losses = -meta_returns[meta_returns < 0] * 100
    meta_var = week6hw.percent_var(meta_returns, 0.95) * -100  # Convert to positive
    meta_es = week6hw.es(losses=meta_losses, alpha=0.95)
    assert meta_es > meta_var, "ES should be larger than VaR for META"
