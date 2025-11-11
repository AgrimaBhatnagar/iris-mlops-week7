import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

class IrisModel:
    def __init__(self):
        iris = load_iris()
        X, y = iris.data, iris.target
        self.clf = LogisticRegression(max_iter=500)
        self.clf.fit(X, y)

    def predict(self, X):
        import numpy as np
        X = np.array(X)
        return self.clf.predict(X).tolist()

model = IrisModel()
