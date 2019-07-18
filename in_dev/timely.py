import time
start = time.strftime('%H:%M')
print (start)


def market_closed:
    if (start>= "16:00"):
        os.system("say The Market is now closed.")
        os.system("say Today You banked:" + )
        os.system("say See you tomorrow")
        exit(0)
