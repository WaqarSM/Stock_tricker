import requests
import urllib.request
import urllib.error
import time
from bs4 import BeautifulSoup
from termcolor import colored
import sched, time
import os
import webbrowser

#-------------------------------------------------------------------------------
def CurrentValue(TickerSym, printval):
    try:
        url = 'https://web.tmxmoney.com/quote.php?qm_symbol='+TickerSym
        response = requests.get(url)
    except equests.exceptions.RequestException as e:
        print('1Error code: ', e.code)
    except urllib.error.URLError as e:
        print('Sleeping 120 seconds...')
        time.sleep(120)
    else:
        # print (response)
        soup = BeautifulSoup(response.text, "html.parser")
        soup.findAll('span')
        one_a_tag = soup.findAll('span')[0]
        if(printval==True):
            print (TickerSym+": $ " ,one_a_tag.text)
        return float(one_a_tag.text)
        # link = one_a_tag['href']

def tickout(TickerSym,principal,numstock):
    global total_cash_money_in_da_bank
    current_net=(CurrentValue(TickerSym, True)-principal)*numstock
    total_cash_money_in_da_bank = total_cash_money_in_da_bank + current_net
    if(current_net>0):
        print (colored("⬆ "+TickerSym+": $ "+str(current_net) , 'green'))
    else:
        print (colored("⬇ "+TickerSym+": $ "+str(current_net) , 'red'))

def HitPrice(TickerSym, price_wanted, buysell):
    if((CurrentValue(TickerSym, False)<=price_wanted) and buysell=="buy"):
        beep = lambda x: os.system("echo \$ '\a';sleep 0.05;" * x)
        beep(15)
        os.system( "say " + TickerSym + " is currently selling at " + str(price_wanted) + "or less")
        print(TickerSym + " is currently selling at " + str(price_wanted) + " or less")
    if((CurrentValue(TickerSym, False)>=price_wanted) and buysell=="sell"):
        beep = lambda x: os.system("echo \$ '\a';sleep 0.05;" * x)
        beep(15)
        os.system( "say " + TickerSym + " is currently selling at " + str(price_wanted) + "or more")
        print(TickerSym + " is currently selling at " + str(price_wanted) + " or more")

def market_closed():
    if ((time.strftime('%H:%M'))>= "16:00"):
        os.system("say The Market is now closed.")
        os.system("say Today You banked:" + str(total_cash_money_in_da_bank) +"Dollars. ")
        os.system("say See you tomorrow")
        print("say The Market is now closed.")
        print("say Today You banked:" + str(total_cash_money_in_da_bank) +"Dollars. ")
        print("say See you tomorrow")
        exit(0)


def timed_beat(sc):
    global total_cash_money_in_da_bank
    total_cash_money_in_da_bank=0
    print("\n30 seconds later... ")
    # $SHOP
    principal_shop=416.56
    numstock_shop=4
    tickout("SHOP",principal_shop,numstock_shop)
    # principal_net_shop=numstock_shop*principal_shop
#--
    # $GLDN.v
    principal_GLDN=0.135
    numstock_GLDN=7600
    tickout("GLDN",principal_GLDN,numstock_GLDN)
    HitPrice("GLDN",0.160,"sell")

    # $BU.TO
    principal_GLDN=1.09 #Saddly own.
    numstock_GLDN=100
    tickout("BU",principal_GLDN,numstock_GLDN)
    HitPrice("BU",1.200,"sell") #Order in


    if (total_cash_money_in_da_bank>0):
        print(colored(("💰 Banking: $ %f" % total_cash_money_in_da_bank),'green'))
        if (total_cash_money_in_da_bank>120):
            os.system( "say THE MARKETS ARE BOOMING RIGHT NOW FAM! Broke 120 dollars today!")
            webbrowser.open("https://www.myinstants.com/media/sounds/ka-ching.mp3")

    else:
        print(colored("😭 Banking: $ %f" % total_cash_money_in_da_bank,'red'))
    market_closed()
    print("-----------------------------")
    s.enter(30, 1, timed_beat, (sc,))

#-------------------------------------------------------------------------------

total_cash_money_in_da_bank=0
# $SHOP
principal_shop=416.56
numstock_shop=4
tickout("SHOP",principal_shop,numstock_shop)
# principal_net_shop=numstock_shop*principal_shop

# $GLDN.v
principal_GLDN=0.135
numstock_GLDN=7600
tickout("GLDN",principal_GLDN,numstock_GLDN)

# $BU.TO
principal_GLDN=1.09
numstock_GLDN=100

tickout("BU",principal_GLDN,numstock_GLDN)

if (total_cash_money_in_da_bank>0):
    print(colored(("💰 Banking: $ %f" % total_cash_money_in_da_bank),'green'))
else:
    print(colored("😭 Banking: $ %f" % total_cash_money_in_da_bank,'red'))
print("-----------------------------")

#-----------------------Looper------------------------------
s = sched.scheduler(time.time, time.sleep)
s.enter(30, 1, timed_beat, (s,))
s.run()
