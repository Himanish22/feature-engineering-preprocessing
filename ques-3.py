import numpy as np

N = 12
vector_x = np.array([14, 16, 20, 25, 31, 36, 40, 45, 27, 21, 34, 38])
vector_y = np.array([12, 15, 19, 24, 30, 35, 39, 43, 26, 20, 33, 37])

mean_x = np.mean(vector_x)
mean_y = np.mean(vector_y)

covariance = np.sum((vector_x - mean_x) * (vector_y - mean_y)) / (N - 1)

variance_x = np.var(vector_x, ddof=1)
variance_y = np.var(vector_y, ddof=1)

correlation = covariance / np.sqrt(variance_x * variance_y)

print(f'Vector X (1x{N} vector): {vector_x}')
print(f'Vector Y (1x{N} vector): {vector_y}')
print(f'Correlation: {correlation:.4f}')
