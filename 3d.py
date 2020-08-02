#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:15:09 2019

@author: rudramani
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from glob import glob
import numpy as np
sns.set()

d = 'Flux-time-Galli.dat'

fin2 = pd.read_csv(d,delimiter='\s+', usecols =[0], header=None)
index = list(fin2[1:][0].values)
index

indices = []
for j in index:
    x = j+'_x'
    y = j+'_y'
    z = j+'_z'
    indices.append([x,y,z])

fnames = glob('*[0-9].dat')
Zi = []
for data in fnames:
   resid = data[0:-4]
   resid =[resid+'_x',resid+'_y',resid+'_z']
   fin = pd.read_csv(data,delimiter='\s+', usecols =[0,1,2], header=None)
   #fin = fin[fin[2]> -20]
   #fin = fin[fin[2]< 20]
   fin
   z = fin
   z.columns = [resid]
   Zi.append(z)
   
Zout = pd.concat(Zi, axis=1)
Zout.head()


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
for k in range(len(indices)):
    D = Zout[indices[k]]
    x = indices[k][0]
    y = indices[k][1]
    z = indices[k][2]
    
    D = D[(D[z]>-10) & (D[z]<10)]
    D = D[(D[x]>-45) & (D[x]<45)]
    D = D[(D[y]>-45) & (D[y]<45)]
    ax.scatter(D[x],D[y],D[z])

    



plt.xticks(range(-45,45,15),fontsize=15,fontweight='bold')

    

plt.yticks(range(-45,45,15),fontsize=15,fontweight='bold')


  
plt.setp(ax.get_zticklabels(), fontsize=15, fontweight="bold")




###### next way
    

fnames=[i+'.dat' for i in index]
Zi = []
for data in fnames:
   resid = data[0:-4]
   resid =['x','y','z']
   fin = pd.read_csv(data,delimiter='\s+', usecols =[0,1,2], header=None)
   #fin = fin[fin[2]> -20]
   #fin = fin[fin[2]< 20]
   fin
   z = fin
   z.columns = [resid]
   Zi.append(z)
   
Zout2 = pd.concat(Zi, axis=0,ignore_index=True)
D2= Zout2



D2 = D2[(D2['z']>-10) & (D2['z']<10)]
D2 = D2[(D2['x']>-45) & (D2['x']<45)]
D2 = D2[(D2['y']>-45) & (D2['y']<45)]
x=D2['x'].values
y=D2['y'].values
z=D2['z'].values
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z, marker='o')


sns.jointplot(x="x", y="y", data=D2, kind="kde");

df=D2
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df.x, df.y, ax=ax)
plt.xticks(range(-45,45,15),fontsize=15,fontweight='bold')
plt.yticks(range(-45,45,15),fontsize=15,fontweight='bold')



sns.rugplot(df.x, color="g", ax=ax)
sns.rugplot(df.y, vertical=True, ax=ax);



f, ax = plt.subplots(figsize=(6, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True);
plt.xticks(range(-45,45,15),fontsize=15,fontweight='bold')
plt.yticks(range(-45,45,15),fontsize=15,fontweight='bold')
















