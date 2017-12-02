from mean_reversion import *

from twitter_connection import *


def lambda_handler(event, context):

    start = event["start"]
    end = event["end"]

    last_data_date = str(get_data('AAPL', get_date_str(-7), get_date_str(1)).tail(1).index.date[0])

    buy_stocks = []
    sell_stocks = []

    yesterday = get_date_str(-1)

    if last_data_date == get_date_str(-1):
        # grab complete list of tickers if date check is passed
        url = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?api_key=KapYhbV5ziJVKXGakJQC&qopts.columns=ticker&date=2017-10-11"
        t = requests.get(url)
        lists = t.json()['datatable']['data']
        tickers = []
        for i in lists:
            for x in i:
                tickers.append(x)
        for i in tickers[start:end]:
            sleep(.2)
            data = get_data(i, get_date_str(-126), get_date_str(1))
            sma = moving_average_df(20, data=data)
            lma = moving_average_df(80, data=data)
            df = inner_join(sma, lma)
            try:
                greater_crossover_columns(df, 0, 1)
            except:
                pass
            try:
                buy_sell_column(df)
            except:
                pass
            try:
                if df.buy_sell.tail(1).item() == 'Buy':
                    buy_stocks.append(i)
                elif df.buy_sell.tail(1).item() == 'Sell':
                    sell_stocks.append(i)
                else:
                    pass
            except:
                pass
    else:
        pass

    #### tweet out list of buy stocks ###

    if len(buy_stocks) == 0:
        pass
    else:
        tweet("Hello! Based on Yesterday's Stock Market Close - {}, above"
              " are stocks that have buy signals based on a Mean Reversion Strategy:".format(yesterday))
        for i in buy_stocks:
            tweet("${} #{} https://www.stockbacktest.io/meanreversion/result/{}/2017-01-01/2019-03-09/20/80".format(i, i, i))

    #### tweet out list of sell stocks ###

    if len(sell_stocks) == 0:
        pass
    else:
        tweet("Hello! Based on Yesterday's Stock Market Close - {}, above"
              " are stocks that have sell signals based on a Mean Reversion Strategy:".format(yesterday))
        for i in sell_stocks:
            tweet("${} #{} https://www.stockbacktest.io/meanreversion/result/{}/2017-01-01/2019-03-09/20/80".format(i, i, i))



