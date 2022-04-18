# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:14:10 2022

@author: hp
"""

from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn import metrics
dataset=datasets.load_diabetes()
model=GaussianNB()
model.fit(dataset.data, dataset.target)
y_pred=model.predict(dataset.data)
print(metrics.confusion_matrix(dataset.target,y_pred))
print(metrics.accuracy_score(dataset.target,y_pred))
