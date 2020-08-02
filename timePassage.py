#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:24:00 2019

@author: rudramani
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from glob import glob
import numpy as np
import mplcursors

fin = pd.read_csv('Flux-time.dat',delimiter='\s+', header=None)
fin = fin[[0,1]][1:]
fin.columns = ['Resid','PassageTime']
fin['PassageTime'] = fin['PassageTime'].astype(float)/25

N = fin['PassageTime'].values
d = fin['PassageTime'].values
ax=sns.kdeplot(d,shade=True, color="r", bw = 2.7)
ax.tick_params(labelsize=12)
#plt.xlim([0, 14])
plt.xticks(range(-15,70,10))
plt.title("Mutacin",fontsize= 18)
plt.xlabel("Time (ns)",fontsize=15)
plt.axvline(6,color = "black", dash_capstyle= 'butt',ls='--')
plt.text(7,0.01,"6 ns",fontsize=15)
plt.show()

######## All The Three At the Same Time:
f1 = pd.read_csv('Flux-time.dat',delimiter='\s+', header=None)
f1 = f1[[0,1]][1:]
f1.columns = ['Resid','PassageTime']
f1['PassageTime'] = f1['PassageTime'].astype(float)/25
d1 = f1['PassageTime'].values

f2 = pd.read_csv('Flux-time-NVB.dat',delimiter='\s+', header=None)
f2 = f2[[0,1]][1:]
f2.columns = ['Resid','PassageTime']
f2['PassageTime'] = f2['PassageTime'].astype(float)/25
d2 = f2['PassageTime'].values

f3 = pd.read_csv('Flux-time-Nisin.dat',delimiter='\s+', header=None)
f3 = f3[[0,1]][1:]
f3.columns = ['Resid','PassageTime']
f3['PassageTime'] = f3['PassageTime'].astype(float)/25
d3 = f3['PassageTime'].values



m1 = f1['PassageTime'].median()
m2 = f2['PassageTime'].median()
m3 = f3['PassageTime'].median()


m1 = f1['PassageTime'].mean()
m2 = f2['PassageTime'].mean()
m3 = f3['PassageTime'].mean()

plt.figure(figsize=(10,5))
ax=sns.kdeplot(d1,  bw = 3, label="Mutacin", lw =3)

ax=sns.kdeplot(d2,  bw = 2, label ="NVB302",lw=3)

ax=sns.kdeplot(d3, bw = 2, label="Nisin",lw=3)


plt.yticks([0,0.02,0.04,0.06,0.08],fontsize = 15)
ax.tick_params(labelsize=15)
plt.xticks(range(0,80,10))
plt.xlabel("Time (ns)",fontsize=15)



plt.text(40,0.06,"15.6 ns",fontsize=15, color = "blue")


plt.text(40,0.055,"10.6 ns",fontsize=15, color = "green")


plt.text(40,0.05,"12.0 ns",fontsize=15, color = "red")
plt.text(30,0.055,"Mean:> ",fontsize=15, color = "Black")



plt.show()