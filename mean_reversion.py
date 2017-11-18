from datetime import datetime, timedelta
from time import sleep
import quandl
import numpy as np
import pandas as pd

import requests
import json

#quandl key#
quandl.ApiConfig.api_key = 'LUc6i68JzC1xFUsauSDm'


def get_date_str(N):
    return str((datetime.now() + timedelta(days=N)).date())


##quick check to see if the last available data was yesterday
def get_data(security, start_date, end_date):
    return quandl.get("WIKI/{}.11".format(security), start_date=start_date, end_date=end_date)


def moving_average_df(ma, data):
    return pd.DataFrame(data['Adj. Close'].rolling(window=ma, center=False).mean().dropna())


def inner_join(df1, df2):
    return pd.concat([df1, df2], axis=1, join='inner')


def greater_crossover_columns(df, col1, col2):
    greater = []
    for s, l in zip(df.ix[:, col1], df.ix[:, col2]):
        if s > l:
            greater.append('Yes')
        else:
            greater.append('No')
    df['greater'] = greater

    crossover = []
    for a, b in zip(df.shift(1).greater, df.greater):
        if a == b:
            crossover.append('No')
        else:
            crossover.append('Yes')
    crossover[0] = 'No'
    df['crossover'] = crossover


def buy_sell_column(df):
    buy_sell = []
    for a, b in zip(df.greater, df.crossover):
        if a == 'No' and b == 'Yes':
            buy_sell.append('Sell')
        elif a == 'Yes' and b == 'Yes':
            buy_sell.append('Buy')
        else:
            buy_sell.append('Hold')
    df['buy_sell'] = buy_sell
