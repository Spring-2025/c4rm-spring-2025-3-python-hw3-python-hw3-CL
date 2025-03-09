from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd

# Starter for week 6 homework with function stubs


def get_stock_data(symbol, start="2020-01-01", end="2025-02-01"):
    """
    Retrieve stock data from Yahoo Finance.
    
    Args:
        symbol: Stock ticker symbol
        start: Start date in YYYY-MM-DD format
        end: End date in YYYY-MM-DD format
        
    Returns:
        Pandas Series of adjusted close prices
    """
    # TODO: Add your code here
    pass


def get_returns(pricevec):
    """
    Calculate returns from a vector of prices.
    
    Args:
        pricevec: Array-like of prices
        
    Returns:
        Array of returns calculated as (price_t / price_t-1) - 1
    """
    # TODO: Add your code here
    pass


def percent_var(r, alpha):
    """
    Calculate the percentage Value at Risk (VaR) for a given confidence level.
    
    Args:
        r: Array of returns
        alpha: Confidence level (e.g., 0.95 for 95%)
        
    Returns:
        VaR as a percentage (negative number representing loss)
    """
    # TODO: Add your code here
    pass


def es(losses, alpha=None, VaR=None):
    """
    Calculate the Expected Shortfall (ES) of losses.
    
    Args:
        losses: Array of positively stated loss values
        alpha: Confidence level (e.g., 0.95 for 95%)
        VaR: Dollar value specifying the VaR threshold
        
    Returns:
        Expected Shortfall as the average of losses exceeding VaR
    """
    # TODO: Add your code here
    pass 