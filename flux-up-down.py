#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:13:07 2019

@author: rudramani
"""

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


######## All The Three At the Same Time:
data = ['Flux-time.dat','Flux-time-NVB.dat','Flux-time-Nisin.dat']

Li = []
for d in data:
    f1 = pd.read_csv(d,delimiter='\s+', header=None)
    f1 = f1[[0,1,2]][1:]
    f1.columns = ['Resid','PassageTime','Direction']
    f1['PassageTime'] = f1['PassageTime'].astype(float)/25
    d1 = f1['PassageTime'].values
    U1 = f1[f1['Direction']=='U']
    D1 = f1[f1['Direction']=='D']
    TU = U1['PassageTime'].mean()
    TD = D1['PassageTime'].mean()
    df = pd.DataFrame({'Up No.':[len(U1)],'Down No.':[len(D1)],\
                       'Time Up':[TU],'Time Down':[TD]})
    Li.append(df)
    
Df = pd.concat(Li)
Df.index=['Mutacin','NVB302','Nisin']
Df['DownFlux'] = Df['Down No.']/Df['Time Down']
Df['UpFlux'] = Df['Up No.']/Df['Time Up']
Df = Df[['Down No.','Up No.', 'Time Down', 'Time Up','DownFlux', 'UpFlux']]

f1 =pd.DataFrame()
f1[['Down','Up']] = Df[['Down No.','Up No.']]
f1.plot.bar(rot =0)

plt.tick_params(labelsize=12)
plt.ylabel("No. of Water Molecules", fontsize =15, fontweight = 'bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
legend_properties = {'weight':'bold','size': 12}
plt.legend(prop=legend_properties, loc = "upper center")
plt.show()

f1 =pd.DataFrame()
f1[['Down','Up']] = Df[['Time Down','Time Up']]
f1.plot.bar(rot =0)

plt.tick_params(labelsize=12)
plt.ylabel("Average Time (ns)", fontsize =15, fontweight = 'bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
legend_properties = {'weight':'bold','size': 12}
plt.legend(prop=legend_properties, loc = "upper center")
plt.show()

f1 =pd.DataFrame()
f1[['Down','Up']] = Df[['DownFlux','UpFlux']]
f1.plot.bar(rot =0)


plt.tick_params(labelsize=12)
plt.ylabel("No. of Water Molecules per ns", fontsize =15, fontweight = 'bold')
plt.xticks(fontweight='bold')
plt.yticks(range(5),fontweight='bold')
legend_properties = {'weight':'bold','size': 12}
plt.legend(prop=legend_properties, loc = "upper center")
plt.show()



o



