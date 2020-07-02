#!/usr/bin/env python
# encoding: utf-8
from decimal import Decimal
import math
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

def factor(N):
    #if N == 0 or N == 1:
    #   return 1
    #else: 
    #   total = 1
    #   for i in range(2,N+1):
    #       total *= i
    #   return total 
    return Decimal(math.factorial(N))
       
#plt.ylabel('Energy (eV/molecule)')
Na = [300, 3000]
Nb = [200, 2000]
q  = [100, 1000]
i = 0
fig1, axarr = plt.subplots(2)
#box = np.matrix('0,0;0,1')
box = [0,1]
for Ni,Nj,qi in zip(Na,Nb,q):
   X = []
   Y = []
   fac1 = factor(Ni-1)
   fac2 = factor(Nj-1)
   S1=[]
   S2=[]
   S3=[]
   for om in range(qi+1):
       X.append(om)
       y1 = factor(Ni+om-1)/factor(om)/fac1
       y2 = factor(Nj+qi-om-1)/factor(qi-om)/fac2
       Y.append(np.multiply(y1,y2))
   Y = np.array(Y)
   Y = Y/sum(Y)
   axarr[box[i]].plot(X,Y)  
   axarr[box[i]].text(qi/10,max(Y)/8*7, '$N_a$='+str(Ni))
   axarr[box[i]].text(qi/10,max(Y)/8*6, '$N_b$='+str(Nj))
   axarr[box[i]].text(qi/10,max(Y)/8*5, '$q_a$='+str(qi))
   axarr[box[i]].set_xlim(0, qi)
 
   i = i + 1
axarr[1].set_xlabel('$q_a$')
axarr[0].set_ylabel('$P$')
axarr[1].set_ylabel('$P$')
#fig1.subplots_adjust(hspacedd=0.3)
fig1.savefig('Einstein2.pdf')

Na = [300, 600, 3000, 6000]
Nb = [200, 400, 2000, 4000]
q = 100
i = 0
fig1, axarr = plt.subplots(2,2)
box = np.matrix('0,0;0,1;1,0;1,1')

for Ni,Nj in zip(Na, Nb):
   X = []
   Y = []
   fac1 = factor(Ni-1)
   fac2 = factor(Nj-1)
   for om in range(q+1):
       X.append(om)
       y1 = factor(Ni+om-1)/factor(om)/fac1
       y2 = factor(Nj+q-om-1)/factor(q-om)/fac2
       Y.append(y1*y2)
   axarr[box[i,0],box[i,1]].bar(X,Y)  
   #axarr[box[i,0],box[i,1]].set_title('$N_a$='+str(Ni)+',$N_b$='+str(Nj))
   axarr[box[i,0],box[i,1]].text(q/10,max(Y)/8*7,'$N_A$='+str(Ni))
   axarr[box[i,0],box[i,1]].text(q/10,max(Y)/8*6,'$N_B$='+str(Nj))
   axarr[box[i,0],box[i,1]].text(q/10,max(Y)/8*5,'$q_A$='+str(q))
   axarr[box[i,0],box[i,1]].set_xlim(0, q)
   i = i + 1
axarr[1,0].set_xlabel('$q_A$')
fig1.subplots_adjust(hspace=0.3)
fig1.savefig('Einstein.pdf')

Na = 300
Nb = 200
q  = 100
fig2 = plt.figure()
fac1 = factor(Na-1)
fac2 = factor(Nb-1)
X=[]
S1=[]
S2=[]
S3=[]
for om in range(q+1):
    X.append(om)
    y1 = math.log(factor(Na+om-1)/factor(om)/fac1)
    y2 = math.log(factor(Nb+q-om-1)/factor(q-om)/fac2)
    S1.append(y1) 
    S2.append(y2) 
    S3.append(y1+y2)
plt.plot(X,S1,label='$S_A$')  
plt.plot(X,S2,label='$S_B$')  
plt.plot(X,S3,label='$S$(total)')  
plt.legend(loc="upper left")
plt.xlabel('$q_A$',fontsize=20)
plt.ylabel('$S/k$',fontsize=20)
#plt.title('$N_A$=300, $N_B$=200, $q$(total)=100')
fig2.savefig('Einstein3.pdf')



Na = [10, 15, 30, 100]
q = 10
i = 0
fig1, axarr = plt.subplots(2,2)
box = np.matrix('0,0;0,1;1,0;1,1')

for Ni in Na:
   X = []
   Y = []
   fac1 = factor(Ni-1)
   for om in range(q+1):
       X.append(om)
       y1 = factor(Ni+om-1)/factor(om)/fac1
       Y.append(y1)
   Y = np.array(Y)
   axarr[box[i,0],box[i,1]].bar(X,Y)  
   axarr[box[i,0],box[i,1]].set_title('$N$='+str(Ni))
   axarr[box[i,0],box[i,1]].get_yaxis().get_major_formatter().set_scientific(True)
   axarr[box[i,0],box[i,1]].yaxis.set_major_formatter(mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False))
   axarr[box[i,0],box[i,1]].set_xlim(0, q+1)
   i = i + 1
axarr[1,0].set_xlabel('$q$')
fig1.subplots_adjust(hspace=0.3)
fig1.savefig('Einstein0.pdf')


