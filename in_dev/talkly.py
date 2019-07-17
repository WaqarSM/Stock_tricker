# from sympy import symbols
# from sympy.plotting import textplot
# # x = symbols('x')
# x=[0,1,2,3,4,2,1,3,4,3]
# textplot(x,0,5)


# import asciiplotlib as apl
# import numpy
#
# x = numpy.linspace(0, 2 * numpy.pi, 10)
# y = numpy.sin(x)
#
# fig = apl.figure()
# fig.plot(x, y, label="data", width=50, height=15)
# fig.show()


import os
beep = lambda x: os.system("echo -n '\a';sleep 0.05;" * x)
beep(15)
ticker="SHOP"
price=345.10
os.system( "say " + ticker + " is currently selling at " + str(price))
