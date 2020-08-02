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




fnames = glob('*[0-9].dat')

Zi = []
for data in fnames:
   resid = data[0:-4]
   fin = pd.read_csv(data,delimiter='\s+', usecols =[2], header=None)
   #fin = fin[fin[2]> -20]
   #fin = fin[fin[2]< 20]
   z = fin
   z.columns = [resid]
   Zi.append(z)
   
Zout = pd.concat(Zi, axis=1)
Zout.head()

   
   

##### calculation the index having bin size n   
def counter(Array):
    n = 0
    for i in Array:
        if i ==0:
            n +=1
    return n/len(Array)*100




Li = {}
for i in Zout.columns:
    b=Zout[i]
    #b = b[(b> -15) & (b < 15)]
    #plt.figure()
    a = plt.hist(b, bins = 10,range=(-5,5))
    if counter(a[0]) < 10:
        Li[i]= counter(a[0])
        
        
ID = [a for a,b in Li.items()]
for a in ID:
    plt.figure(figsize =(15,2))
    #plt.xlim(a[1]-500,a[2]+500)
    plt.ylim(-15,15)
    plt.plot(Zout[a])
    plt.title(a)

df = Zout[ID]
df = df[(df> -15) & (df < 15)]


#######################################
#### This is the Main Block for calculation
    
   
Fi = {}

 
for i in Zout.columns:
    df = Zout[i]
    k = 0 
    l = int(len(df)/10)
    for j in  range(10):
        DfSliceList = df[k:l] 
        f1 = DfSliceList[(DfSliceList>= -5) & (DfSliceList <= 5)]
        f1 = f1.dropna(axis=0)
        R = f1.max() - f1.min()
        if R > 7:
            Fi[i] = (k,l)

            print(i)
            print("POOO")
            print(R)
    
        k += 750 
        l +=750
       
len(Fi)

outfile = open('Nai.txt','w') ## to make empty
outfile = open('Nai.txt','a')
for m,n in Fi.items():
    data = (int(m),n[0],n[1])
    outfile.write(m+".dat"+"\t"+str(n[0])+"\t"+str(n[1]))
    #outfile.write(str(data))
    outfile.write("\n")
outfile.close()



for a, b in Fi.items():
    y = a
    print(y)
    plt.figure(figsize =(25,3))
   
    plt.xlim(b[0]-1000,b[1]+1000)
    plt.ylim(-20,20) ### should be phosphate COM
    plt.plot(Zout[y])
    plt.title(a)
    plt.axhline(y=14, color='r', linestyle='-')
    plt.axhline(y=-14, color='r', linestyle='-')
    plt.show()
    

 ####### Main Calculation Ends here   
 
plt.plot(Zout['333'])
plt.xlim(600,6000)
    
    
### Applying Bin filter            

Bi = {}
for a,b in Fi.items():
    s = a
    
    b=Zout[s]
    #b = b[(b> -15) & (b < 15)]
    plt.figure()
    a = plt.hist(b, bins = 10,range=(-5,5))
    plt.title(s)
    if counter(a[0]) < 100: ### bin with empty percentage
        Bi[s]= counter(a[0])
        
len(Bi)
ID = [a for a,b in Bi.items()]



           

''' Reference Codes   

     
len(Fi)
for j in Fi:
    print(j[1])
    y = j[0]
    x = [m for m in range(j[1],j[2])]
    plt.figure(figsize=(10, 3))
    #plt.ylim(-5.1,6.5)
    #plt.scatter(x,Zout['1012'])
    plt.xlim(j[1],j[2])
    plt.plot(Zout[y])
    plt.title(j)

plt.plot(Zout[j]    







Status = []  

Zout = pd.concat(Zi, axis=1)
df = Zout
df = df[(df> -5) & (df < 5)]
df.dropna(axis=0)

df['1012'].dropna(axis=0)



Chireko = []



for i in Zout.columns:
    Status = [] 
    for j in Zout[i]:
        if j >= 14:
            Status.append(2)
            
        elif  (j < 14) and (j >= 5):
            Status.append(1)
            
        elif  (j < 5) and (j >= -3):
            Status.append(0)
            
        elif  (j < -3) and (j >= -10):
            Status.append(-1)
        

            
            
        elif  j< -10:
            Status.append(-2)
        

    
    Sorted = []
    for k in range(len(Status)-1):
        if Status[k] == Status[k+1]:
            c = k
        else:
            d= k
            Sorted.append(Status[d])

    for l in range(len(Sorted)-4):
        if (Sorted[l] == 2) and (Sorted[l+1] == 1) and (Sorted[l+2] == 0)  and (Sorted[l+3] == -1) :
            print('Down',i)
            Chireko.append(i)
        if (Sorted[l] == 1) and (Sorted[l+1] == 0) and (Sorted[l+2] == -1)  and (Sorted[l+3] == -2) :
            print('Down',i)
            Chireko.append(i)
            
        elif (Sorted[l] == -2) and (Sorted[l+1] == -1) and (Sorted[l+2] == 0)  and (Sorted[l+3] == 1):
            print('up',i)
            Chireko.append(i)
        elif (Sorted[l] == -1) and (Sorted[l+1] == 0) and (Sorted[l+2] == -1)  and (Sorted[l+3] == -2):
            print('up',i)
            Chireko.append(i)

x = [j for j in range(7500)]        
for i in Chireko:
    #Zout = Zout[(Zout> -5) & (Zout < 10)]
    plt.figure(figsize = (12,2))
   
    #plt.scatter(x,Zout[i])
    plt.plot(Zout[i])
    plt.ylim(-15,15)
    plt.title(i)
len(Chireko)

'''