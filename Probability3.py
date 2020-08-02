#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:47:20 2019

@author: rudramani
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 08:29:38 2019

@author: rudramani
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from glob import glob
import numpy as np
plt.style.use('seaborn-deep')



data = ['Mutacin-no.dat','NVB302-no.dat','Nisin-no.dat']

    
####
    
z =data   
f1 = pd.read_csv(z[0],delimiter='\s+', header=None)
f1.columns = ['Time', 'MU1140']
f2 = pd.read_csv(z[1],delimiter='\s+', header=None)
f2.columns = ['Time','NVB302']
f3 = pd.read_csv(z[2],delimiter='\s+', header=None)
f3.columns = ['Time','Nisin']

plt.figure(figsize =(8,5))
plt.hist([f1['MU1140'], f2['NVB302'], f3['Nisin']],bins = 40,label=['MU1140', 'NVB302','Nisin'],rwidth=100)
plt.xlabel("Number of Water Molecules at Z : [-5,5]", fontsize =15)
plt.ylabel("Frequency", fontsize =15)
plt.xticks(range(1,46,5))
plt.tick_params(labelsize=15)
plt.legend(loc='upper right')
plt.show()
#######

f = [f1['MU1140'],f2['NVB302'],f3['Nisin']]
plt.figure(figsize =(8,5))
for w in f:
    N= w
    
    ax=sns.kdeplot(N,shade=True, bw = 0.5)
    ax.tick_params(labelsize=15)
    #plt.xlim([0, 14])
    plt.xticks(range(0,45,5))
    plt.xlabel("Number of Water Molecules at Z : [-5,5]", fontsize =15)
    plt.show()


######
f1 =f1.iloc[:7500]
f2 =f2.iloc[:7500]
f3 =f3.iloc[:7500]
from collections import Counter
Di1 = dict(Counter(f1["MU1140"]))
Di2 = dict(Counter(f2["NVB302"]))
Di3 = dict(Counter(f3["Nisin"]))

Dic = [Di1,Di2,Di3]
List_Al = []
for y in Dic:
    Nt = sum(y[key] for key in y)
    List_p = [[] for i in range(2)]
    for key in  sorted(y.keys()):
        p= y[key]/Nt
        ln_p = -np.log1p(p)
        List_p[0].append(key)
        List_p[1].append(ln_p)
    List_Al.append(List_p)

plt.figure(figsize=(10,5))
label=['MU1140', 'NVB302','Nisin']

for arr in List_Al:
    #plt.figure(figsize=(8,5))    
    b = plt.scatter(arr[0],arr[1],s=150)
    b = plt.plot(arr[0],arr[1])
    plt.ylim([-0.3,0])
    plt.xticks(range(0,50,5),fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("N",fontsize=15)
    plt.ylabel("-lnP(N)",fontsize=15,labelpad=5)
    #plt.title("Mutacin")
    plt.show()
plt.text(4.5,-0.25,"Mutacin",color ="blue",fontsize=15) 
plt.text(10,-0.145,"NVB302",color ="green",fontsize=15)
plt.text(25,-0.05,"Nisin",color ="red",fontsize=15)   
    

    
    
    
    
    
