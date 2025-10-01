import numpy as np
from cvxopt import matrix, solvers

class SVM:
    def __init__(self):
        self.w = None  # Weights
        self.b = None  # Bias

    def fit(self, X, y):
   
        n_samples, n_features = X.shape

       
        y = y.reshape(-1, 1) * 1.0

        # matrices for QP solver
        K = np.dot(X, X.T) * (y @ y.T) 
        P = matrix(K)
        q = matrix(-np.ones((n_samples, 1)))
        G = matrix(-np.eye(n_samples))
        h = matrix(np.zeros(n_samples))
        A = matrix(y.T)
        b = matrix(np.zeros(1))

        # quadratic programming problem
        solvers.options['show_progress'] = False
        solution = solvers.qp(P, q, G, h, A, b)


        alphas = np.array(solution['x']).flatten()

        # non-zero Lagrange multipliers
        sv = alphas > 1e-5
        self.alphas = alphas[sv]
        self.sv_X = X[sv]
        self.sv_y = y[sv]

        #  (w)
        self.w = np.sum(self.alphas[:, None] * self.sv_y * self.sv_X, axis=0)

        #  (b)
        self.b = np.mean(self.sv_y - np.dot(self.sv_X, self.w))

    def predict(self, X):
        return np.sign(np.dot(X, self.w) + self.b)


if __name__ == "__main__":

    X = np.array([[2, 3], [1, 1], [2, 1], [5, 6], [6, 6], [6, 7]])
    y = np.array([-1, -1, -1, 1, 1, 1])  

    # Train
    svm = SVM()
    svm.fit(X, y)

    # Predictions
    X_test = np.array([[3, 3], [4, 5]])
    predictions = svm.predict(X_test)
    print(f"Predictions: {predictions}")
