# -*- coding: utf-8 -*-
"""
Least squares anomaly detection in sequences.

Example of detecting periods of abnormality in a time series of physiological
measurements.

Created on Fri Apr 12 13:34:28 2013

@author: John Quinn <jquinn@cit.ac.ug>
"""
import numpy as np
import lsanomaly
import scipy.signal
import pylab as plt
        
# Use electrocardiogram data from PhysioNet as an example.
# More data can be downloaded from http://www.physionet.org/cgi-bin/ATM
# Select MIT-BIH Arrhythmia Database (mitdb), and export as CSV.
X = np.loadtxt('data/MIT_physionet_sample.csv',skiprows=2, 
               usecols=(1,2), delimiter=',')
X[:,0] = X[:,0] - scipy.signal.medfilt(X[:,0],kernel_size=301)
X[:,1] = X[:,1] - scipy.signal.medfilt(X[:,1],kernel_size=301)

# Construct 4-D  observations from the original 2-D data: values at the
# current index and at a fixed lag behind.
N = X.shape[0]
lag = 10
X2 = np.zeros((N-lag,4))
for i in range(lag,N):
    X2[i-lag,0] = X[i,0]
    X2[i-lag,1] = X[i-lag,0]
    X2[i-lag,2] = X[i,1]
    X2[i-lag,3] = X[i-lag,1]   
    
X_train = X2[:5000,:]
X_test = X2[10000:15000,:]

# Train the model
anomalymodel = lsanomaly.LSAnomaly(rho=1, sigma=.5)
anomalymodel.fit(X_train)

# Predict anomalies statically (assuming iid samples)
y_pred_static = anomalymodel.predict_proba(X_test)

# Predict anomalies sequentially (assume known transition matrix and
# initial probabilities)
A = np.array([[.999, .001],[.01, .99]])
pi = np.array([.5,.5])
y_pred_dynamic = anomalymodel.predict_sequence(X_test, A, pi)

plt.clf()
plt.subplot(4,1,1)
plt.plot(X_test[:,1])
plt.ylabel('ECG 1',rotation='horizontal')
plt.grid(which='major',axis='x')
plt.xticks(plt.xticks()[0],'')
plt.title('Detection of cardiac arrhythmia from ECG sequence')
plt.subplot(4,1,2)
plt.plot(X_test[:,3])     
plt.grid(which='major',axis='x')
plt.xticks(plt.xticks()[0],'')
plt.ylabel('ECG 2',rotation='horizontal')
plt.subplot(4,1,3)
plt.plot(y_pred_static[:,1],'r')
plt.xticks(plt.xticks()[0],'')
plt.grid(which='major',axis='both')
plt.ylim([-.05,1.05])
plt.ylabel('Anomaly score\n(static)',rotation='horizontal')
plt.subplot(4,1,4)
plt.plot(y_pred_dynamic[:,1],'r')  
plt.grid(which='major',axis='both')
plt.ylim([-.05,1.05])
plt.ylabel('Anomaly score\n(dynamic)',rotation='horizontal')
plt.show()
    
    