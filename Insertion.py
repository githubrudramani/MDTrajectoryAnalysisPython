#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:38:44 2020

@author: rudramani
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set()

#DataList = ['L.dat','LM.dat'] #,'M.dat','MM.dat','S.dat','SM.dat']
DataList = ['M.dat','MM.dat']
#DataList = ['S.dat','SM.dat']
Aminos = [32,32,29,29,25,25]
#name = ['22-40','22-40M'] #,'25-40','25-40M','29-40','29-40M']
name =['25-40','25-40M']
#name =['29-40','29-40M']
for data in DataList:
    #j = Aminos[DataList.index(data)]
    j = 29
    z = name[DataList.index(data)]
    f = pd.read_csv(data,delimiter='\s+', header=None)[1:]
    idx = f.iloc[0:j,2]
    In = list(idx)
    f = f[[3,4,5]]
    ResList = []
    for i in range(j):
        n = len(f.iloc[i::j, :])
        dat = f.iloc[i::j, :]   ###.sum()/n
        dat = dat.astype(float)
        m = dat[5][0:2500]
        ResDf = pd.DataFrame({str(i+1):m})
        ResDf.index = range(0,2500)
        ResList.append(ResDf)

   
    
    Df = pd.concat(ResList, axis = 1)
    Df.columns = Df.columns.astype(int)
    init = Df[0:152]
    final = Df[2375:2500]
    plt.figure(figsize=(10,5))
    legend_properties = {'weight':'bold','size':17}
    sns.pointplot(data =init, join=False,ci ='sd',color ="blue",capsize =0.1, label = "first 50ns")

    sns.pointplot(data =final, join=False,ci ='sd',color ="green",capsize =0.1)
    plt.ylabel("Distance ($Å$)",fontsize=20,fontweight='bold')
    plt.xlabel("Resid",fontsize=20,fontweight='bold')
    plt.yticks(range(2,32,4),fontsize = 20,fontweight='bold')
    plt.title(z,fontsize = 20, fontweight = 'bold')
    #plt.legend(["fist 50ns", "last 50ns"],prop=legend_properties)
   