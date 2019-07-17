import requests
import urllib.request
import urllib.error
import time
from bs4 import BeautifulSoup
from termcolor import colored
import sched, time
import os






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

def HitPrice(TickerSym, price_wanted):
    if(CurrentValue(TickerSym, False)<=price_wanted):
        beep = lambda x: os.system("echo \$ '\a';sleep 0.05;" * x)
        beep(15)
        os.system( "say " + TickerSym + " is currently selling at " + str(price_wanted) + "or less")
        print(TickerSym + " is currently selling at " + str(price_wanted) + " or less")

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
    principal_GLDN=0.135 #DO NOT OWN YET
    numstock_GLDN=7600
    tickout("GLDN",principal_GLDN,numstock_GLDN)
    HitPrice("GLDN",0.135) #Order in

    # $BU.TO
    principal_GLDN=1.09 #Saddly own.
    numstock_GLDN=100
    tickout("BU",principal_GLDN,numstock_GLDN)


    if (total_cash_money_in_da_bank>0):
        print(colored(("💰 Banking: $ %f" % total_cash_money_in_da_bank),'green'))
    else:
        print(colored("😭 Banking: $ %f" % total_cash_money_in_da_bank,'red'))
    print("-----------------------------")
    s.enter(30, 1, timed_beat, (sc,))

#-------------------------------------------------------------------------------
try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
    from pip.operations import freeze

x = freeze.freeze()
for p in x:
    print (p)



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
