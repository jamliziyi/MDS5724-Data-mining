# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 23:47:16 2022

@author: Neal LONG
Modify the code to count the errors and number of nodes for decision tree 
which requires at least 2 samples in any leaf nodes, and with 
maximum depth from  [2,3,4,5,6,7,8,9,10], but random_state is always set to 0 

Note:
1. Only use three features 'sepal length (cm)', 'sepal width (cm)',  'petal length (cm)'
2. Only set the random_state to 0, and the parameters which control 
    "minimum number of samples required to be at a leaf node" and "maximum depth "as required, with other settings as default values
"""


from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load data
iris = load_iris()    
# Determine feature matrix X and target array Y
X = iris.data[:,[0,1,2]]
Y_true = iris.target


Nodes  = []
depths = [2,3,4,5,6,7,8,9,10]
for depth in depths:
    clf = DecisionTreeClassifier(random_state=0,min_samples_leaf=2,max_depth=depth)
    clf.fit(X, Y_true)
    Y_Pred = clf.predict(X)
    erro = sum(Y_Pred!=Y_true)
    Nodes.append(erro)
    print("max depth:",depth)
    print("This trained decision tree has {} nodes, and {} errors".format(clf.tree_.node_count, erro))
    print("*"*50)

Nodes  = []
depths = [2,3,4,5,6,7,8,9,10]
for depth in depths:
    clf = DecisionTreeClassifier(random_state=0,min_samples_leaf=2,max_depth=depth)
    clf.fit(X, Y_true)
    Y_Pred = clf.predict(X)
    erro = clf.tree_.node_count + sum(Y_Pred!=Y_true)
    Nodes.append(erro)
    print("max depth:",depth)
    print("This trained decision tree has {} nodes, and {} errors".format(clf.tree_.node_count, erro))
    print("*"*50)

Nodes  = []
depths = [2,3,4,5,6,7,8,9,10]
for depth in depths:
    clf = DecisionTreeClassifier(random_state=0,min_samples_leaf=2,max_depth=depth)
    clf.fit(X, Y_true)
    Y_Pred = clf.predict(X)
    erro = 0.3*clf.tree_.node_count + sum(Y_Pred!=Y_true)
    Nodes.append(erro)
    print("max depth:",depth)
    print("This trained decision tree has {} nodes, and {} errors".format(clf.tree_.node_count, erro))
    print("*"*50)
