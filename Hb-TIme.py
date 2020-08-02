import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set()


data = ['HB-L.dat','HB-LM.dat','HB-M.dat','HB-MM.dat','HB-S.dat','HB-SM.dat']


plt.figure(figsize =(7,5))
for i in data:
      f  = pd.read_csv(i,delimiter='\s+', header=None)
      #idx= f[0][1:31]
      #idx = idx.astype(float)
      #f = f.iloc[1:31,0:2]
      f = f.astype(float)
      f = f.rolling(window=200).mean()
      f[0] = f[0]/12500
      plt.plot(f[0],f[1], lw =2)

legend_properties = {'weight':'bold','size':17}
#plt.xlabel("Distance ($\AA$)",fontsize=18,fontweight='bold',labelpad=-3)
plt.xlabel("Time ($\mu$s)",fontsize=18,fontweight='bold',labelpad=0)
#plt.xticks([300,350,400,450,500],fontsize = 18,fontweight='bold')
plt.xlim(0,1)
plt.yticks(fontsize = 18,fontweight='bold')
plt.xticks(fontsize = 18,fontweight='bold')
plt.ylabel("No of H-Bonds",fontsize=20,fontweight='bold')
plt.legend(['L','LM','M','MM','S','SM'],\
           prop=legend_properties,  borderaxespad=0, framealpha=0, ncol=2)
#plt.title("Distance of Pyrophosphate moiety from first ring",fontsize=20,fontweight='bold' )

### ENERGY plot

data = ['E-L.dat','E-LM.dat','E-M.dat','E-MM.dat','E-S.dat','E-SM.dat']


plt.figure(figsize =(8,5))
for i in data:
      f  = pd.read_csv(i,delimiter='\s+', header=None)[[2,3,4]][1:]
      #idx= f[0][1:31]
      #idx = idx.astype(float)
      #f = f.iloc[1:31,0:2]
      f = f.astype(float)
    
      f.index = f.index/6250
      f = f.rolling(window=100).mean()
      f.columns = ['Elec','VDW','Total']
      
      plt.plot(f.index,f.Total, lw =2)

legend_properties = {'weight':'bold','size':17}
#plt.xlabel("Distance ($\AA$)",fontsize=18,fontweight='bold',labelpad=-3)
plt.xlabel("Time ($\mu$s)",fontsize=18,fontweight='bold',labelpad=0)
#plt.xticks([300,350,400,450,500],fontsize = 18,fontweight='bold')
plt.xlim(0,1)
plt.ylim(-475,-200)
plt.yticks( fontsize = 18,fontweight='bold')
plt.xticks(fontsize = 18,fontweight='bold')
plt.ylabel("TE (kCal/mol)",fontsize=20,fontweight='bold',labelpad=-1)
plt.legend(['L','LM','M','MM','S','SM'],\
           prop=legend_properties,  borderaxespad=0, framealpha=0, ncol=3, loc = "upper left")
#plt.title("Distance of Pyrophosphate moiety from first ring",fontsize=20,fontweight='bold' )

### Density data
data = ['L_density.dat','M_density.dat']
#data = ['WT_L/rmsd.dat','WT_M/rmsd.dat']
plt.figure(figsize =(8,5))
for i in data:
      f  = pd.read_csv(i,delimiter='\s+', header=None)
      #idx= f[0][1:31]
      #idx = idx.astype(float)
      #f = f.iloc[1:31,0:2]
      f = f.astype(float)
      #f[0]=f[0]*0.435
    
      
      #f = f.rolling(window=100).mean()
      #f.columns = ['Z', 'Water Density']
      
      #plt.plot(f['Z'],f['Water Density'], lw =2)
      plt.plot(f[0],f[1], lw =3)

legend_properties = {'weight':'bold','size':17}
plt.xlabel("Z ($\AA$)",fontsize=18,fontweight='bold',labelpad=-3)
#plt.xlabel("Time (ns)",fontsize=20,fontweight='bold',labelpad=0)
#plt.xticks([300,350,400,450,500],fontsize = 18,fontweight='bold')
plt.xlim(-15,15)
plt.ylim(0,0.008)
plt.yticks([0.00, 0.002,0.004,0.006,0.008], fontsize = 18,fontweight='bold')
plt.xticks(fontsize = 18,fontweight='bold')
plt.ylabel("Water Density",fontsize=20,fontweight='bold',labelpad=0)
plt.legend(['L-Pentamer','M-Pentamer'],\
           prop=legend_properties,  borderaxespad=0, framealpha=0, ncol=3, loc = "center")
#plt.title("Distance of Pyrophosphate moiety from first ring",fontsize=20,fontweight='bold' )


### TSV Radius of pore plots'
####### Load data from allFrame
## for L
data = ['hole'+str(i)+'.tsv' for i in range(200,574)]

data


Li = []
for i in data:
      f  = pd.read_csv(i,delimiter='\s+', header=None)
      f = f[[0,1]]
      f = f.astype(float)
      Li.append(f)


df = pd.concat(Li, axis = 1)
R1 =[]
R2 =[]
S1 = []
for index,row in df.iterrows():
    n = len(row[0].dropna())
    r = row[0].dropna().sum()/n
    n2 = len(row[1].dropna())
    r2 = row[1].dropna().sum()/n
    s = row[1].dropna().std()
    
    R1.append(r)
    R2.append(r2)
    S1.append(s)
S1 = [x for x in S1 if str(x) !='nan']
len(R1)
R1 = R1[0:len(S1)]
R2 = R2[0:len(S1)]



#for M
data = ['hole'+str(i)+'.tsv' for i in range(200,574)]
data


Li = []
for i in data:
      f  = pd.read_csv(i,delimiter='\s+', header=None)
      f = f[[0,1]]
      f = f.astype(float)
      Li.append(f)


df = pd.concat(Li, axis = 1)
R3 =[]
R4 =[]
S2 = []
for index,row in df.iterrows():
    n = len(row[0].dropna())
    r = row[0].dropna().sum()/n
    n2 = len(row[1].dropna())
    r2 = row[1].dropna().sum()/n
    R3.append(r)
    R4.append(r2)
    s = row[1].dropna().std()
    S2.append(s)
    
S2 = [x for x in S2 if str(x) !='nan']
len(S2)
R3 = R3[0:len(S2)]
R4 = R4[0:len(S2)]


plt.figure(figsize =(7,4))

plt.errorbar(R1,R2, yerr = S1, errorevery= 2, elinewidth= 0.7, capsize= 1, lw =3)
plt.errorbar(R3,R4, yerr = S2, errorevery= 2, elinewidth= 0.5, capsize= 1, lw =3)

legend_properties = {'weight':'bold','size':17}
plt.xlabel("Z ($\AA$)",fontsize=18,fontweight='bold',labelpad=-3)
#plt.xlabel("Time (ns)",fontsize=20,fontweight='bold',labelpad=0)
#plt.xticks([300,350,400,450,500],fontsize = 18,fontweight='bold')
#plt.xlim(-20,20)
plt.ylim(1.5,10.5)
plt.yticks([2,4,6,8,10], fontsize = 18,fontweight='bold')
plt.xticks(fontsize = 18,fontweight='bold')
plt.ylabel("Radius ($\AA$)",fontsize=20,fontweight='bold',labelpad=0)
plt.legend(['L-Pentamer','M-Pentamer'],\
           prop=legend_properties,  borderaxespad=0, framealpha=0, loc = (0.3,0.6),  ncol=1)
#plt.title("Distance of Pyrophosphate moiety from first ring",fontsize=20,fontweight='bold' )
