__author__ = '310176470'

from sklearn.svm import OneClassSVM
import pandas as pd

# dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')
train_data = pd.read_csv("subject_1.csv", header=0, index_col=1, parse_dates=[1])
test_data = pd.read_csv("subject_2.csv", header=0, index_col=1, parse_dates=[1])

# print(train_data)

clf = OneClassSVM()
output_training = clf.fit(train_data)

print(output_training)

print(test_data)

# for data in test_data:
# 	if clf.predict(data) < 0:
# 		print(data)
