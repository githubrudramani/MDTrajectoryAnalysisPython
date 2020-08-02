#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:13:01 2019

@author: rudramani
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from glob import glob
import numpy as np
import mplcursors
from collections import Counter
import re



data = ['Nisin-no14.dat','NVB302-no14.dat','Mutacin-no14.dat']

Li = []
for d in data:
    f1 = pd.read_csv(d,delimiter='\s+', header=None)
    f1 = f1[[1]][1:7500]
    Li.append(f1)
Df = pd.concat(Li,axis =1)
Df.columns =['Nisin','NVB302','Mutacin']
Df.index = Df.index/25


Df.plot(figsize =(10,5))
plt.tick_params(labelsize=12)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

legend_properties = {'weight':'bold','size': 12}
plt.legend(prop=legend_properties, loc = "upper center")
plt.xlabel("Time (ns)", fontsize = 15, fontweight = 'bold')
plt.ylabel("No of Water Molecules", fontsize = 15, fontweight = 'bold')
plt.show()


data = ['hbonds-Nisin.dat','hbonds-NVB.dat','hbonds-Mut.dat']

Li = []
for d in data:
    f1 = pd.read_csv(d,delimiter='\s+', header=None)
    f1 = f1[[1]][1:7500]
    Li.append(f1)
Df = pd.concat(Li,axis =1)
Df.columns =['Nisin','NVB302','Mutacin']
Df.index = Df.index/25


Df.plot(figsize =(10,5),legend=True,linewidth=0.5,color =['blue','green','red'])
plt.tick_params(labelsize=12)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

legend_properties = {'weight':'bold','size': 12}
plt.legend(prop=legend_properties, loc = "upper center")
plt.xlabel("Time (ns)", fontsize = 15, fontweight = 'bold')
plt.ylabel("No of H-Bonds", fontsize = 15, fontweight = 'bold')
plt.show()