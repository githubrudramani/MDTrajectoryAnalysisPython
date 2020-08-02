#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:36:02 2020

@author: rudramani
"""


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_excel("Oragenics.xlsx")


columns = ['Name','Mean RGYR',"SASA Hydrophilic", "SASA Hydrophobic",'Hydrophilic dipole moment',\
           'Hbonds W/ water']
df = df[columns]
df = df.dropna(axis =0)
df = df[0:6]
name = df.Name
D = df[['Mean RGYR',"SASA Hydrophilic", "SASA Hydrophobic",'Hydrophilic dipole moment','Hbonds W/ water']]
D.columns = ['RGYR',"Hydophilic SASA","Hydrophobic SASA", "Hydrophilic Dipole Moment","Hbonds W/water"]
D["SASA Ratio (Philic/Phobic)"] = D["Hydophilic SASA"]/D["Hydrophobic SASA"]
D = D[['RGYR','Hbonds W/water', 'SASA Ratio (Philic/Phobic)', 'Hydrophilic Dipole Moment']]
D.index = name
for j in D.columns:
    plt.figure(figsize=(6,5))
    D[j].plot.bar()
    plt.xticks(fontsize = 12, weight ='bold', rotation = 30)
    plt.yticks(fontsize = 12, weight ='bold')
    plt.ylabel(j,fontsize = 15, weight ='bold', labelpad = -1)

    
 
