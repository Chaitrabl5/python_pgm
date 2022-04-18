# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:33:26 2022

@author: hp
"""
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('kmeans.csv')
x1=data['x'].values
x2=data['y'].values
x=np.matrix(list(zip(x1,x2)))
plt.scatter(x1,x2)
plt.show()
Mark=['s','o','v']
clf=KMeans(n_clusters=3).fit(x)
for i,t in enumerate(clf.labels_):
    plt.plot(x1[i],x2[i],marker=Mark[t])
