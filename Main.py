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

        print(ticker_list)

    @staticmethod
    def get_features():
        while True:
            feature_list = []

            print("Please enter a 1 for each feature you would like, and a 0 for a feature you wish to ignore.\n")
            feature_input = input("|Open|\t|Prev Close|\t|Market Cap|\t|P/E Ratio (ttm)|\n")

            match_feature_input = str(re.match('^[0-1]*$', feature_input))

            if len(feature_input) == 4 and match_feature_input != 'None':
                feature_list.append(feature_input)
                break
            elif len(feature_input) != 4:
                print("You entered too many values. Please try again.\n\n")
            elif match_feature_input == 'None':
                print("You may only enter a '1' or a '0'. Please try again.\n\n")

        print(feature_list)


gather_info.get_tickers()
gather_info.get_features()