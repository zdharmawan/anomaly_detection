__author__ = '310176470'

import lsanomaly
import numpy as np

X_train = np.array([[1.1],[1.3],[1.2],[1.05]])
X_test = np.array([[1.15],[3.6],[1.25]])

anomalymodel = lsanomaly.LSAnomaly()

anomalymodel.fit(X_train)
anomalymodel.predict(X_test)
# anomalymodel.predict_proba(X_test)

