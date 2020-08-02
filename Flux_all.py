#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:26:11 2019

@author: rudramani
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 07:17:46 2019

@author: rudramani
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from glob import glob
import numpy as np
import mplcursors



## Mutacin
M = glob('*[0-9].dat')
Zi = []
for data in M:
   resid = data[0:-4]
   fin = pd.read_csv(data,delimiter='\s+', usecols =[2], header=None)
   #fin = fin[fin[2]> -20]
   #fin = fin[fin[2]< 20]
   z = fin
   z.columns = [resid]
   Zi.append(z)
   
Mout = pd.concat(Zi, axis=1)

### NVB302

Nv = glob('*[0-9].dat')
Zi = []
for data in Nv:
   resid = data[0:-4]
   fin = pd.read_csv(data,delimiter='\s+', usecols =[2], header=None)
   #fin = fin[fin[2]> -20]
   #fin = fin[fin[2]< 20]
   z = fin
   z.columns = [resid]
   Zi.append(z)
   
Nvout = pd.concat(Zi, axis=1)

###  Nisin

Ni = glob('*[0-9].dat')
Zi = []
for data in Ni:
   resid = data[0:-4]
   fin = pd.read_csv(data,delimiter='\s+', usecols =[2], header=None)
   #fin = fin[fin[2]> -20]
   #fin = fin[fin[2]< 20]
   z = fin
   z.columns = [resid]
   Zi.append(z)
   
Niout = pd.concat(Zi, axis=1)
############


Mi = {}

 
for i in Mout.columns:
    df = Mout[i]
    k = 0 
    l = int(len(df)/10)
    for j in  range(10):
        DfSliceList = df[k:l] 
        f1 = DfSliceList[(DfSliceList>= -5) & (DfSliceList <= 5)]
        f1 = f1.dropna(axis=0)
        R = f1.max() - f1.min()
        if R > 9:
            Mi[i] = (k,l)

            print(i)
            print("POOO")
            print(R)
    
        k += 750 
        l +=750
       
len(Mi)



Nvi = {}
for i in Nvout.columns:
    df = Nvout[i]
    k = 0 
    l = int(len(df)/10)
    for j in  range(10):
        DfSliceList = df[k:l] 
        f1 = DfSliceList[(DfSliceList>= -5) & (DfSliceList <= 5)]
        f1 = f1.dropna(axis=0)
        R = f1.max() - f1.min()
        if R > 9:
            Nvi[i] = (k,l)

            print(i)
            print("POOO")
            print(R)
    
        k += 750 
        l +=750
       
len(Nvi)


Ni = {}
for i in Niout.columns:
    df = Niout[i]
    k = 0 
    l = int(len(df)/10)
    for j in  range(10):
        DfSliceList = df[k:l] 
        f1 = DfSliceList[(DfSliceList>= -5) & (DfSliceList <= 5)]
        f1 = f1.dropna(axis=0)
        R = f1.max() - f1.min()
        if R > 9:
            Ni[i] = (k,l)

            print(i)
            print("POOO")
            print(R)
    
        k += 750 
        l +=750
       
len(Ni)




for a, b in Fi.items():
    y = a
    plt.figure(figsize =(25,3))
   
    plt.xlim(b[0]-1000,b[1]+1000)
    plt.ylim(-20,20) ### should be phosphate COM
    plt.plot(Zout[y])
    plt.title(a)
    plt.axhline(y=14, color='r', linestyle='-')
    plt.axhline(y=-14, color='r', linestyle='-')
    plt.show()
    
