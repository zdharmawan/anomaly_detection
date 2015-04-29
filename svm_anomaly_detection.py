__author__ = '310176470'

from sklearn.svm import OneClassSVM
import pandas as pd
import numpy as np

date_spec = {'timestamp': [1]}

train_data = pd.read_csv("subject_1.csv", header=0, index_col=1, parse_dates=[1])
test_data = pd.read_csv("subject_4.csv", header=0, index_col=1, parse_dates=[1])
# train_data = pd.read_csv("subject_1.csv", header=0, index_col=0, parse_dates=date_spec)
# test_data = pd.read_csv("subject_4.csv", header=0, index_col=0, parse_dates=date_spec)

## print(train_data)
# remove from training data : bp_systolic,bp_diastolic,drink_coffee,eating,sleeping,exercise
# del train_data['bp_systolic']
# del train_data['bp_diastolic']
del train_data['drink_coffee']
del train_data['eating']
del train_data['sleeping']
del train_data['exercise']
del train_data['minute']
del train_data['second']
# print(train_data)

## print(test_data)
# remove from testing data : bp_systolic,bp_diastolic,drink_coffee,eating,sleeping,exercise
# del test_data['bp_systolic']
# del test_data['bp_diastolic']
del test_data['drink_coffee']
del test_data['eating']
del test_data['sleeping']
del test_data['exercise']
del test_data['minute']
del test_data['second']
print(test_data)

clf = OneClassSVM()
output_training = clf.fit(train_data)

y_pred = clf.predict(test_data)
# print(y_pred)

i = 0
for idx, data in enumerate(y_pred):
  	if data > 0:
		print(idx, data)
		print(train_data.iloc[[idx]])
		i += 1

print(i)