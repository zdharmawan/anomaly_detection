# -*- coding: utf-8 -*-
"""
Demo of least squares anomaly detection on static digits data.

In this example, we try to recognise digits of class 9 given training
examples from classes 0-8.

Created on Fri Apr 12 13:34:28 2013

@author: John Quinn <jquinn@cit.ac.ug>
"""
import lsanomaly
from sklearn import datasets, cross_validation, metrics
import numpy as np

digits = datasets.load_digits()
X = digits.data
y = digits.target

# Split data into training and test sets, then remove all examples of
# class 9 from the training set, leaving only examples of 0-8.
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X, y, test_size=0.5)

train_inlier_idx = y_train<9
X_train = X_train[train_inlier_idx,:]
y_train = y_train[train_inlier_idx]

# Fit the model for inlier classes
anomalymodel = lsanomaly.LSAnomaly()
anomalymodel.fit(X_train,y_train)

# Use the outlier score as a prediction of whether each test point
# belongs to class 9, for which no training data was given.    
predictions = anomalymodel.predict_proba(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test==9, predictions[:,-1])
print('AUC=%f' % (metrics.auc(fpr,tpr)))

# Try to assign each test point to classes 0-9, given only test data
# for classes 0-8.
y_pred = anomalymodel.predict(X_test)
y_pred = [w if np.isreal(w) else 9 for w in y_pred]
print 'Confusion matrix for all classes:'
print metrics.confusion_matrix(y_test, y_pred)
    