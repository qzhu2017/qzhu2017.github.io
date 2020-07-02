#!/usr/bin/env python
# encoding: utf-8
from decimal import Decimal
import math
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def factor(N):
    #if N == 0 or N == 1:
    #   return 1
    #else: 
    #   total = 1
    #   for i in range(2,N+1):
    #       total *= i
    #   return total 
    return Decimal(math.factorial(N))
 
N = [10, 15, 30, 100]
i = 0
fig1, axarr = plt.subplots(2,2)
box = np.matrix('0,0;0,1;1,0;1,1')
axarr[0,0].set_title('Flipping coins')

for Ni in N:
   X = []
   Y = []
   for om in range(Ni+1):
       X.append(om)
       Y.append(factor(Ni)/factor(Ni-om)/factor(om))
   #print X, Y, str(Ni)
   axarr[box[i,0],box[i,1]].bar(X,Y)  
   axarr[box[i,0],box[i,1]].set_title('$N$='+str(Ni))
   axarr[box[i,0],box[i,1]].set_xlim(0, Ni)
   axarr[box[i,0],box[i,1]].get_yaxis().get_major_formatter().set_scientific(True)
   axarr[box[i,0],box[i,1]].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))
   i = i + 1
fig1.subplots_adjust(hspace=0.3)

#plt.title('Coumarin-V')
#plt.xlabel('Phonon frequncy[cm$^{-1}$]')
#legend = plt.legend(loc='upper right')
fig1.savefig('flip.pdf')
