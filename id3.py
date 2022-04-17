# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:24:48 2022
id3 decision tree
@author: hp
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn import tree
import pydotplus
iris=datasets.load_iris()
x=iris.data
y=iris.target
clf=DecisionTreeClassifier(criterion='entropy')
model=clf.fit(x, y)
dot_data=tree.export_graphviz(clf,outfile=None, class_names=iris.target_names)
graph=pydotplus.graph_from_dot_file(dot_data)
graph.write_png(tree.jpg)