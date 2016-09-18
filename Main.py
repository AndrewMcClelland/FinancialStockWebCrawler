__author__ = 'Andrew McClelland'

import pandas as pd
import os
import time
import re
import urllib.request

class gather_info:
    @staticmethod
    def get_tickers():
        ticker_list = []
        loop_cond = 0

        while loop_cond != 1:
            temp_ticker_input = str(input("Please enter desired stock, followed by a carriage return:\n")).upper()

            URL_resp = str(urllib.request.urlopen('https://finance.yahoo.com/quote/' + temp_ticker_input + '?ltr=1').read())

            if 'Try looking again!</span></span>' in URL_resp:  # invalid stock ticker
                print("The stock you entered is incorrect. Please try again.\n")
            else:
                ticker_list.append(temp_ticker_input)
                loop_cond = 1

        while True:
            temp_ticker_input = str(input("If you are done entering stocks, please enter ~. Otherwise, enter another stock.\n")).upper()

            URL_resp = str(urllib.request.urlopen('https://finance.yahoo.com/quote/' + temp_ticker_input + '?ltr=1').read())

            if temp_ticker_input == '~':
                break
            elif 'Try looking again!</span></span>' in URL_resp:  # invalid stock ticker
                print("The stock you entered is incorrect. Please try again.\n")
            else:
                ticker_list.append(temp_ticker_input)

        return ticker_list

    @staticmethod
    def get_desired_features():
        while True:

            print("Please enter a 1 for each feature you would like, and a 0 for a feature you wish to ignore.\n")
            feature_input = input("|Open|\t|Prev Close|\t|Market Cap|\t|P/E Ratio (ttm)|\n")

            match_feature_input = str(re.match('^[0-1]*$', feature_input))

            if len(feature_input) == 4 and match_feature_input != 'None':
                feature_list = feature_input
                break
            elif len(feature_input) != 4:
                print("You entered too many values. Please try again.\n\n")
            elif match_feature_input == 'None':
                print("You may only enter a '1' or a '0'. Please try again.\n\n")

        feature_list = list(str(feature_list))
        return feature_list

    @staticmethod
    def get_features():

        desired_tickers = gather_info.get_tickers()
        desired_features = gather_info.get_desired_features()

        for each_ticker in desired_tickers:

            yahoo_url_source = str(urllib.request.urlopen('https://finance.yahoo.com/quote/' + each_ticker + '?ltr=1').read())

            if desired_features[0] == '1':  # Open price
                open_price = yahoo_url_source.split('$OPEN.1">')[1].split('</td></tr>')[0]

            if desired_features[1] == '1':  # Prev close price
                prev_close_price = yahoo_url_source.split('$PREV_CLOSE.1">')[1].split('</td></tr>')[0]

            if desired_features[2] == '1':  # Market cap
                market_cap = yahoo_url_source.split('$MARKET_CAP.1">')[1].split('</td></tr>')[0]

                if "B" in market_cap:
                    market_cap = float(market_cap.replace('B', '')) * 1000000000
                elif "M" in market_cap:
                    market_cap = float(market_cap.replace('M', '')) * 1000000

            if desired_features[3] == '1':  # P/E ratio
                pe_ratio = yahoo_url_source.split('$PE_RATIO.1">')[1].split('</td></tr>')[0]

gather_info.get_features()