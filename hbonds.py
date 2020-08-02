#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:48:16 2019

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

fin = pd.read_csv('HB-SM-detail.dat',delimiter='\s+', header=None)
fin = fin[2:]
#L,LM = 6
# M = 5
#MM = 5
# S = 6
#SM = 7
Don ={}
Accp = {}
for index, row in fin.iterrows():
    if row[0].startswith("LIP"):
        pass
    else:
        r2 = row[2].replace("%",'')
        r2 = float(r2)
        if row[0] not in Don:
            Don[row[0]] = r2
        else:
            Don[row[0]] += r2
    if row[1].startswith("LIP"):
        pass
    else:
        r2 = row[2].replace("%",'')
        r2 = float(r2)
        if row[1] not in Accp:
            Accp[row[1]] = r2
        else:
            Accp[row[1]] += r2
            


HB = Counter(Don) + Counter(Accp)

Resname = []
Resid = []
for key,value in HB.items():
    a=re.sub('-.*','',key)
    b = a[3:]
    Resname.append(a)
    Resid.append(int(b))
Resname = list(set(Resname))
Resid = list(set(Resid))
#### AMAZING sorting according to any character
Resname = sorted(Resname, key=lambda x: int(x[3:]))

Li = []
for name in Resname:
    n = HB[name+'-Main-N']
    o = HB[name+'-Main-O']
    S = 0
    for key,value in HB.items():
        if name+'-Side' in key:
            S += HB[key]
        else:
            pass
    df = pd.DataFrame({"NH":[n],"CO":[o],"SC":[S],"Total":[n+o+S]})
    name2 = name.replace('CYS','ALA')
    df.index = [name2]
    Li.append(df)
        
Df_HB = pd.concat(Li)            
NorFactor = Df_HB['Total'].sum()
Df_HB = Df_HB[Df_HB["Total"] >= 10].dropna()
cols = ['NH','CO','SC']

Nis= Df_HB["Total"]


legend_properties = {'weight':'bold', "size" :18}
Df_HB[cols].plot(kind='bar', stacked=True,color = ["blue","red","green"],legend = False, width=0.9,figsize=(7,7))
## mutacin figsize=(7,10)
plt.tick_params(labelsize=18)
plt.xticks(fontweight='bold', rotation=45)
plt.yticks(range(0,110,40),fontweight='bold')
#plt.legend(prop=legend_properties, ncol = 1)
plt.show()

