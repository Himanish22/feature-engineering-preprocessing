import numpy as np
N = 10
vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mean = np.mean(vector)

sample_variance = np.var(vector, ddof=1)

population_variance = np.var(vector)

print(f'Array (1x{N} vector): {vector}')
print(f'Mean: {mean:.4f}')
print(f'Sample Variance): {sample_variance:.4f}')
print(f'Population Variance: {population_variance:.4f}')
