import numpy as np
import gnuplotlib as gp
price=[1,2,4,1,3,4,1,2,3,1,2,5]

x = np.linspace(0,len(price),1)

gp.plot( x, price )
# [ graphical plot pops up showing a simple sinusoid ]

# gp.plot( (x, np.sin(x), {'with': 'boxes'}),
#          # (x, np.cos(x), {'legend': 'cosine'}),
#          _with    = 'lines',
#          terminal = 'dumb 80,40',
#          unset    = 'grid')
