#!/usr/bin/python
# <bitbar.title>Stock Ticker</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>Robert Kanter</bitbar.author>
# <bitbar.author.github>rkanter</bitbar.author.github>
# <bitbar.desc>Provides a rotating stock ticker in your menu bar, with color and percentage changes</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>https://i.imgur.com/Nf4jiRd.png</bitbar.image>
# <bitbar.abouturl>https://github.com/rkanter</bitbar.abouturl>
#Ticker gets Stock Price for a list of stocks

# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
from termcolor import colored

# test_tik='GLDN.V'
# print (test_tik,": ", si.get_live_price(test_tik))

# print (colored('hello', 'red'), colored('world', 'green'))

ticker=["GLDN.V","ABX.TO","SHOP"]

hero=si.get_live_price(ticker[0])
print(ticker[0],"\t:\t%.3f"  % hero)
print("---")
# or any other ticker
for i in ticker:
    a=si.get_live_price(i)
    print(i,"\t:\t%.3f"  % a)
    # print (i, "\t:\t", si.get_live_price(i).)
