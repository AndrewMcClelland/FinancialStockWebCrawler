__author__ = 'Andrew McClelland'

import pandas as pd
import os
import time
import re

ticker_list = []

temp_ticker_input = str(input("Please enter desired stock, followed by a carriage return:\n")).upper()

ticker_list.append(temp_ticker_input)

while True:
    temp_ticker_input = str(input("\nIf you are done entering stocks, please enter ~. Otherwise, enter another stock.\n")).upper()
    if temp_ticker_input == '~':
        break
    else:
        ticker_list.append(temp_ticker_input)

print(ticker_list)

for each_ticker in ticker_list:
    yahoo_URL = 'https://finance.yahoo.com/quote/' + each_ticker + '?ltr=1'
    #print(yahoo_URL)

