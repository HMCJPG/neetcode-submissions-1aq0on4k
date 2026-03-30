import numpy as np
from numpy.typing import NDArray


# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)

        predictions = []
        for row in X:

            prediction = 0

            for i in range(3):
                prediction += row[i]*weights[i]
            prediction = round(prediction, 5)
            predictions.append(prediction)

        return predictions



    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        
        n = len(model_prediction)

        total_err = 0
        for i in range(n):
            diff = model_prediction[i] - ground_truth[i]
            diff_sq = diff * diff
            total_err += diff_sq

        mean_err = float(total_err / n)
        mean_err = round(mean_err, 5)

        return mean_err

        
        
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)
