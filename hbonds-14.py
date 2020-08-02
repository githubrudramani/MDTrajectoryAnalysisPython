#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:35:31 2019

@author: rudramani
"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import pandas as pd
from glob import glob
import numpy as np
import mplcursors
from collections import Counter
import re

f1 = pd.read_csv('hbonds-Mut14.dat',delimiter='\s+', header=None)
f2 = pd.read_csv('hbonds-NVB14.dat',delimiter='\s+', header=None)
f3 = pd.read_csv('hbonds-Nisin14.dat',delimiter='\s+', header=None)
f1.index = f1.index/25
f2.index = f2.index/25
f3.index = f3.index/25
plt.figure(figsize =(10,5))

f3[1].plot(label = 'Nisin',legend=True,linewidth=1.0)
f2[1].plot(label = 'NVB302',legend=True,linewidth=1.0)
f1[1].plot(label = 'Mutacin',legend=True,linewidth=1.0)

plt.tick_params(labelsize=12)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

legend_properties = {'weight':'bold','size': 12}
plt.legend(prop=legend_properties, loc = "upper center")
plt.xlabel("Time (ns)", fontsize = 15, fontweight = 'bold')
plt.ylabel("No. of H-Bonds", fontsize = 15, fontweight = 'bold')
plt.show()



#### Diffusion 
Nh = [f1[1].mean(),f2[1].mean(),f3[1].mean()]
Mean = {'Mutacin':15.6,'NVB302':10.6,'Nisin':12.0}
L = 2.8*2.8/12 
Diff = []
for key,value in Mean.items():
   
    Dw = L/value/1000
    Diff.append(Dw)
    
plt.plot(Nh,Diff)
