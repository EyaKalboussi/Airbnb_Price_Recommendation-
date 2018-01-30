from sklearn.linear_model import LogisticRegression
import numpy as np

class Regressor():
    def __init__(self):
        self.reg = LogisticRegression(random_state=61)

    def fit(self, X, y):
        self.reg.fit(X, y)

    def predict(self, X):
        return self.reg.predict(X)