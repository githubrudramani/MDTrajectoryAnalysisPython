#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:49:55 2020

@author: rudramani
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:57:59 2019

@author: rudramani
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:02:55 2019

@author: rudramani
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.spatial import distance
from sklearn.preprocessing import StandardScaler




polar = ['ILA','ILB','LYA','LYB','ASP', 'GLU', 'LYS', 'ARG', 'SER', 'THR', 'TYR', 'HSD', 'CYS', 'ASN', 'GLN','HET']
nonpolar = ['ALA','VAL','PHE','ILE','LEU','PRO','MET','TRP','GLY','DHA','DHB','ABU']


#DataList = ['SASA-A-1.dat','SASA-A-12.dat','SASA-B-1.dat','SASA-B-12.dat']
DataList = ["SASA-OG"+str(i)+".dat" for i in [191,168,179,157,253,161]]




phil = []
phob = []

for data in DataList:
    f = pd.read_csv(data,delimiter='\s+', header=None)
    idx = f.iloc[0:21,0]
    f = f[[1,2]]
    SasaList = []
    for i in range(21):
        n = len(f.iloc[i::21, :])
        dat = f.iloc[i::21, :]   ###.sum()/n
        m = dat[2].sum()/n
        SasaList.append(m)
   
    
    SasaDf = pd.DataFrame(SasaList)
    SasaDf.index = idx.values
    SasaDf.columns =['SASA']
    
    In = list(set(SasaDf.index))
    np = 0
    p = 0
    for i in In:
        if i in nonpolar:
            np += SasaDf.loc[i].values.sum()
            
        else:
            p += SasaDf.loc[i].values.sum()

    r = p #/np  
    d = np #(p-np)/(p+np) 
    phil.append(p)  
    phob.append(np)    

  
        
Df = pd.DataFrame({"philic":phil, "phobic":phob})     

print(Df["phobic"]) 

   





PhilPerPhob = pd.concat(Ratio, axis = 0)
Dispersion = pd.concat(Dispersn, axis = 0)





PhilPerPhob.to_excel('PhilPerPhob3.xlsx')
Dispersion.to_excel('Dispersion3.xlsx')

a =float('Nan')
line = pd.DataFrame({'PHE1':a,'LYS2':a,'TRP4':a,'LEU6':a,'PRO9':a,\
                     'ARG13':a,'PHE17':a  },\
    index=[4.5,8.5,8.51,8.52,8.53,8.54,9.5,10.1,10.2,11.5,\
           14.5])
Dispersion.index = [i for i in range(17)]
milako = pd.concat([Dispersion,line]).sort_index()
milako.to_excel('Phobic-milako.xlsx')






