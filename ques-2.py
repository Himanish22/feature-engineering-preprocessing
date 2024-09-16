import numpy as np

M = 12
vector_x = np.array([15, 8, 12, 21, 27, 39, 48, 32, 18, 22, 29, 34])
vector_y = np.array([17, 9, 14, 24, 28, 41, 45, 33, 20, 23, 30, 36])

mean_x = np.mean(vector_x)
mean_y = np.mean(vector_y)

covariance = np.sum((vector_x - mean_x) * (vector_y - mean_y)) / (M - 1)

print(f'Vector X (1x{M} vector): {vector_x}')
print(f'Vector Y (1x{M} vector): {vector_y}')
print(f'Covariance: {covariance:.4f}')
