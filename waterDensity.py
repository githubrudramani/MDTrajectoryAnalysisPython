#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:08:37 2020

@author: rpokhrel
"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import pandas as pd
from glob import glob
import numpy as np

d = 'residZSM.dat'
fin = pd.read_csv(d,delimiter='\s+', header=None)


plt.figure(figsize =(9,6))
h = fin.hist(bins=50)
plt.xticks(fontsize=15,fontweight='bold')
plt.yticks(fontsize=15,fontweight='bold')
plt.xlabel('z-Coordinate (A)', fontsize = 18,fontweight='bold',labelpad=8)
plt.ylabel('Probability Density', fontsize = 18,fontweight='bold',labelpad=8)
plt.show()



plt.figure(figsize =(9,6))
sns.distplot(fin[0],hist =False, kde =True, 
             kde_kws = {'linewidth': 3},
                 label = '')
#plt.xlim(-38,29)
plt.xticks(fontsize=15,fontweight='bold')
plt.yticks(fontsize=15,fontweight='bold')
plt.xlabel('z-Coordinate (A)', fontsize = 18,fontweight='bold',labelpad=8)
plt.ylabel('Probability Density', fontsize = 18,fontweight='bold',labelpad=8)
plt.show()



count, division = pd.np.histogram(fin[0], bins = 80)
len(count)
division = division[0:-1]
f2 = pd.DataFrame({"coor":division,
                  "freq":count})
#N0 = f2["freq"].sum()
N0= f2["freq"].min()
f2["freq"]=f2["freq"]/N0
f2["freq"] = np.log(f2["freq"])
w = -00.019872* 300

f2["freq"]= f2["freq"]*w
plt.figure(figsize =(9,6))
plt.plot(f2["coor"],f2["freq"], linewidth = 3)
plt.xlim(-38,29)
#plt.xticks(range(-10,10,2),fontsize=15,fontweight='bold')
plt.xticks(fontsize=15,fontweight='bold')
plt.yticks(fontsize=15,fontweight='bold')
plt.xlabel('z-Coordinate (A)', fontsize = 18,fontweight='bold',labelpad=8)
plt.ylabel('Free Energy (kCal/mol)', fontsize = 18,fontweight='bold',labelpad=8)
