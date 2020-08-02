#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:35:59 2020

@author: rudramani
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from glob import glob
import numpy as np
import mplcursors
sns.set()

fin = pd.read_csv('Nisin-expansion.dat',delimiter='\s+', header=None)
fin=fin.rolling(window=50).mean()
x = fin[0]

fin.index =fin.index/25


fin.plot(legend=False,figsize=(8,6))


plt.xlabel("Time (ns)",fontsize=20)
#plt.xlim([-10, 10.1])
#plt.ylim([0, 0.25])
plt.xticks(fontsize = 20)
plt.yticks([-10,-5,0,5,10],fontsize = 20)
plt.ylabel("Distance  ($Å$)",fontsize=20)