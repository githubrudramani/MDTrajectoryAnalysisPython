#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:55:29 2019

@author: rudramani
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from glob import glob
import numpy as np
import mplcursors

fin = pd.read_csv('NVB302-density.dat',delimiter='\s+', header=None)
x = fin[0]
y = fin[1]*100

fin2 = pd.read_csv('mutacin-density.dat',delimiter='\s+', header=None)
x2 = fin2[0]
y2 = fin2[1]*100

fin3 = pd.read_csv('Nisin-density.dat',delimiter='\s+', header=None)
x3 = fin3[0]
y3 = fin3[1]*100

plt.figure(figsize =(8,5))
plt.plot(x,y, label ="NVB302")


plt.plot(x2,y2,label ="MUT1140")

plt.plot(x3,y3,label ="Nisin")


plt.legend(loc='upper center',fontsize = 15)
plt.xlabel("Z (Å)",fontsize=15)
plt.xlim([-10, 10.1])
plt.ylim([0, 0.25])
plt.xticks(range(-10,11,2),fontsize = 15)
plt.yticks(fontsize = 15)
plt.ylabel("Number Density (1/$Å^3$) *100 ",fontsize=15)


plt.show()



