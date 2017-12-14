import pandas as pd
import numpy as np
import cPickle as pkl
from sklearn.decomposition import PCA
from sklearn.metrics import f1_score, make_scorer
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
import matplotlib.pyplot as plt
import utilities
import sys
import os
import gc
import random


X_reduced = pd.read_csv('X_reduced.csv',index_col=0)

labels = pd.read_csv('p1_train.csv', index_col=0)
train = X_reduced.merge(labels, left_index=True, right_index=True)
X = train.drop(['population', 'sequencing_center'], axis=1)
Y = train[['population', 'sequencing_center']]


kf = KFold(n_splits=5)
kf.get_n_splits(X)

## Performing 5 fold cross validation on MLP Classifier
from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
y = mlb.fit_transform(Y.as_matrix())
y = pd.DataFrame(y)
print(kf)  

scaler = StandardScaler()

scores = []
count =1
for train_index, test_index in kf.split(X):
#     print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    X_train = scaler.fit_transform(X_train)

    clf = MLPClassifier(hidden_layer_sizes=(256, 128), activation='tanh', #solver='lbfgs', #learning_rate='adaptive',
                    verbose=False, tol=1e-5 ,max_iter=500, learning_rate_init=0.005
#                     warm_start = True
                   )
    
    clf.fit(X_train, y_train)
    
    X_test = scaler.transform(X_test)
    y_pred = clf.predict(X_test)
    scores.append(f1_score(y_test, y_pred, average='macro'))
    print count,") f1_score : ", scores[-1]
    count+=1