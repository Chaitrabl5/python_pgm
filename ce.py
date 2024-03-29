import numpy as np
import pandas as pd
data=pd.DataFrame(data=pd.read_csv('ce.csv'))
concepts=np.array(data.iloc[:,0:-1])
target = np.array(data.iloc[:,-1])
def learn(concepts, target):
    specific=concepts[0].copy()
    general=[["?" for i in range(len(specific))] for i in range(len(specific))]
    for i,h in enumerate(concepts):
        if target[i]=="yes":
            for x in range(len(specific)):
                if h[x]!=specific[x]:
                    specific[x]='?'
                    general[x][x]='?'
        if target[i]=="no":
            for x in range(len(specific)):
                if h[x]!=specific[x]:
                    general[x][x]=specific[x]            
                else:
                    general[x][x]='?'
    indices=[i for i,val in enumerate(general) if val==['?','?','?','?','?']]                 
    for i in indices:
        general.remove(['?','?','?','?','?'])
    return specific,general 
sf,gf=learn(concepts, target)    
print(sf)
print(gf)