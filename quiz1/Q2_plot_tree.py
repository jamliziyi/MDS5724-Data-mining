# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:47:16 2023

@author: Neal LONG

Modify the code to satisfy:
    1. Only use the 2-dimensional features of iris, i.e., 'sepal length (cm)' and 'petal length (cm)'
    2. Create the decision tree that uses "entropy" as criterion, and set "random_state" to 0,  
       with other settings as default values,  refer to 
       https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
    3. Continue to use the decision tree built as above, but plot its tree structure
       with the depth for plotting (not tree depth) beging set 4
        https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Load data
iris = load_iris()

# Determine feature matrix X and taget array Y
X = iris.data[:,[0,2]]
Y = iris.target

# Create and train decision tree on all 
clf = DecisionTreeClassifier(criterion="entropy",random_state=0)
clf.fit(X, Y)

# Plot tree structure
plt.figure(1, figsize=(12, 12))
plot_tree(clf, filled=True,max_depth=4)
plt.show()

