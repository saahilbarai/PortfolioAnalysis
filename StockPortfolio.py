import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

def sum_checker(Ratios): 
    return sum(Ratios.values()) == 100

def plot_pie(Ratios):
    plt.pie(Ratios.values(), labels=Ratios.keys(), autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.show()

def get_data(Ticker):


def re_balance(Portfolio):

def make_portfolio():




def main():
    Cash = 10000
    Ratios = {
        "Stocks": 5,
        "Snp": 30,
        "REIT": 10,
        "Bonds": 10,
        "EmergingMarkets": 20,
        "SmallCap": 20,
        "Cash": 5
    }

    Category_to_ticker_map = {
        "Stocks": ["PLTR", "TSLA"],
        "Snp": ["FXAIX"],
        "REIR": [],
        "Bonds": [],
        "EmergingMarkets": [],
        "SmallCap": [],
        "Cash": []
    }

    plot_pie(Ratios)    


if __name__ == "__main__":
    main()
