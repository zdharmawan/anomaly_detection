__author__ = '310176470'

from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()

# train_data = pd.read_csv("subject_1.csv", header=0, index_col=1, parse_dates=[1])
# test_data = pd.read_csv("subject_2.csv", header=0, index_col=1, parse_dates=[1])

gnb = GaussianNB()

# print(iris.data)
# print(iris.target)
# y_pred = gnb.fit(train_data, test_data).predict(train_data)
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
