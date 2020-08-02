#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:21:35 2020

@author: rpokhrel
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from glob import glob
import numpy as np
sns.set()




color = ['black', 'blue','green','red','purple','orange','cyan','black']

data = ['WT.pmf','L.pmf','LM.pmf','MM.pmf','MMM.pmf','S.pmf','SM.pmf']
#order = ['29-40','22-40M','25-40M','29-40M','22-40','WT.pmf','25-40']

#data = ['L.pmf','LM.pmf','MM.pmf','MMM.pmf','S.pmf','SM.pmf','WT.pmf']
plt.figure(figsize =(9,5.4))
for i in range(7):
      f  = pd.read_csv(data[i],delimiter='\s+', header=None)
      idx= f[0][1:31]
      idx = idx.astype(float)
      f = f.iloc[1:31,0:2]
      f = f.astype(float)
      plt.plot(f[0],f[1], lw =3, color = color[i], alpha=0.5)

legend_properties = {'weight':'bold','size':20}
plt.xlabel("Z-Coordinate ($\AA$)",fontsize=20,fontweight='bold',labelpad = -4)
plt.xticks(fontsize = 20,fontweight='bold')
plt.xlim(17,-28)
plt.yticks(fontsize = 20,fontweight='bold')
plt.ylabel("Free Energy (kCal/mol)",fontsize=25,fontweight='bold',labelpad = 1)
plt.legend(['WT', 'L','LM','M','MM','S','SM'],loc = (0.1,0.5),prop=legend_properties, ncol = 2,  borderaxespad=0, framealpha=0)
plt.show()



############# waterDensity
#data = ['residZS.dat','residZLM.dat','residZSM.dat','residZL.dat']

data = ['residZL.dat','residZLM.dat','residZM.dat','residZMM.dat','residZS.dat','residZSM.dat']

plt.figure(figsize =(5,3))
for i in data:
      f  = pd.read_csv(i,delimiter='\s+', header=None)
      sns.distplot(f[0],hist =False, kde =True, 
             kde_kws = {'linewidth': 4},
                 label = '')


#plt.ylim([0,0.02,0.04,0.06,0.08])
plt.xlim(0,10)
plt.ylim(0,0.01)
plt.xticks([0,5,10],fontsize=25,fontweight='bold')
plt.yticks([0,0.004,0.008],fontsize=25,fontweight='bold')

plt.xlabel('', fontsize = 18,fontweight='bold',labelpad=-2)
plt.ylabel('', fontsize = 18,fontweight='bold',labelpad=1)
#plt.legend(['L','LM','M','MM','S','SM'],loc = (0.55,0.5),prop=legend_properties, ncol = 2,  borderaxespad=0, framealpha=0)
plt.show()




####################################
plt.figure(figsize =(7,5))
legend_properties = {'weight':'bold','size':15}
for i in data:
      f  = pd.read_csv(i,delimiter='\s+', header=None)
      count, division = pd.np.histogram(f[0], bins = 80)
      division = division[0:-1]
      f2 = pd.DataFrame({"coor":division,
                  "freq":count})
      N0= f2["freq"].min()
      f2["freq"]=f2["freq"]/N0
      f2["freq"] = np.log(f2["freq"])
      w = -00.019872* 300
      f2["freq"]= f2["freq"]*w
      plt.plot(f2["coor"],f2["freq"], linewidth = 3)

#plt.xticks(range(-10,10,2),fontsize=15,fontweight='bold')
plt.xlim(-15,20)
plt.ylim(-57,-15)
plt.xticks(fontsize=15,fontweight='bold')
plt.yticks([-55,-45,-35,-25,-15],fontsize=15,fontweight='bold')
plt.xlabel('Z-Coordinate ($\AA$)', fontsize = 18,fontweight='bold',labelpad=-2)
plt.ylabel('Free Energy (kCal/mol)', fontsize = 18,fontweight='bold',labelpad=1)
plt.legend(['L','LM','M','MM','S','SM'],loc = (0.1,0.85),prop=legend_properties, ncol = 3,  borderaxespad=0, framealpha=0)
plt.show()



