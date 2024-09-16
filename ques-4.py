import numpy as np

M = 5
N = 6

matrix = np.array([
    [2.3, 4.5, 6.1, 3.2, 5.7, 8.9],
    [7.1, 3.8, 4.4, 9.5, 6.3, 2.6],
    [5.2, 8.3, 9.1, 2.5, 4.8, 6.0],
    [10.2, 3.3, 5.8, 7.4, 8.2, 3.1],
    [6.7, 2.9, 4.7, 6.8, 7.5, 5.0]
])

matrix_T = matrix.T

covariance_matrix = np.cov(matrix_T, rowvar=False)

correlation_matrix = np.corrcoef(matrix_T, rowvar=False)

print(f'Matrix (MxN dimension):\n{matrix}\n')
print(f'Covariance Matrix (MxM dimension):\n{covariance_matrix}\n')
print(f'Correlation Matrix (MxM dimension):\n{correlation_matrix}\n')
