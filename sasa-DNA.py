import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set()


data = ['Contact-6og.dat','Contact-covalent.dat','Contact-ort.dat']


plt.figure(figsize =(7,4))
for i in data:
      f  = pd.read_csv(i,delimiter='\s+', header=None)[0:12500]
      #idx= f[0][1:31]
      #idx = idx.astype(float)
      #f = f.iloc[1:31,0:2]
      f = f.astype(float)
      f = f.rolling(window=10).mean()
      f.index = f.index/10
      plt.plot(f[0], lw =2)

legend_properties = {'weight':'bold','size':15}
#plt.xlabel("Distance ($\AA$)",fontsize=18,fontweight='bold',labelpad=-3)
plt.xlabel("Time(ns)",fontsize=15,fontweight='bold',labelpad=-3)
plt.xticks([0, 20,40,60,80,100],fontsize = 15,fontweight='bold')
#plt.ylim(0.9,4.5)
plt.xlim(0,100.1)
plt.yticks([650, 750,850,950,1050],fontsize = 15,fontweight='bold')
plt.ylabel(r'Contact Surface ($\AA^2$)',fontsize=18,fontweight='bold',labelpad=-4)






