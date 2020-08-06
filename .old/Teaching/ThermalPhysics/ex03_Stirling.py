#!/usr/bin/env python
# encoding: utf-8
import math
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

def factor(N):
    if N == 0 or N == 1:
       return 1
    else: 
       total = 1
       for i in range(2,N+1):
           total *= i
       return total 
def gamma(N):
    N_max = 3*N
    numbin = 1000
    xbin = N_max/numbin
    X = np.linspace(0,N_max,num=numbin)
    gam = 0
    for Xi in X:
        gam += pow(Xi,N)*math.exp(-Xi)*xbin

    return gam

#plt.ylabel('Energy (eV/molecule)')
N = xrange(1,50)
fig1, axarr = plt.subplots(2, sharex=True)
X = []

Y11 = []
Y12 = []
Y21 = []
Y22 = []

for Ni in N:
   X0 = factor(Ni)
   X.append(Ni)
   Y11.append(X0)
   Y21.append(math.log(X0))
   Y12.append(pow(Ni,Ni)*math.exp(-Ni)*math.sqrt(2*3.14159*Ni))
   Y22.append(Ni* math.log(Ni) - Ni)
axarr[0].set_title("Stirling's Approximation")
axarr[0].plot(X, Y11, 'r-', label="$N!$")
axarr[0].plot(X, Y12, 'b*', label="$N^Ne^{-N}\sqrt{2{\pi}N}$")  
axarr[0].legend(loc="upper left")
axarr[1].plot(X, Y21, 'rs', label='ln$N!$')
axarr[1].plot(X, Y22, 'b*', label='$N$ln$N - N$')  
axarr[1].legend(loc="upper left")
#axarr[].set_xlim(0, q)
#plt.title('Coumarin-V')
axarr[1].set_xlabel('N')
fig1.savefig('Stirling.pdf')


N = np.linspace(0.0,3.6,num=20)
Y1 = []
Y2 = []
for Ni in N:
    Y1.append(pow(Ni,Ni)*math.exp(-Ni)*math.sqrt(2*3.14159*Ni))
    Y2.append(gamma(Ni))
fig = plt.figure()
plt.plot([0,1,2,3],[1,1,2,6], 'yd', label='$N!$' )
plt.plot(N, Y1, 'r-', label='$\Gamma(n+1)$' )
plt.plot(N, Y2, 'b-', label='$\sqrt{2\pi n}(n/e)^n$' )
plt.legend(loc="upper left")
plt.xlabel("$N$")
fig.savefig('Stirling2.pdf')

