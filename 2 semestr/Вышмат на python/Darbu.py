import numpy as np
from random import sample, randint

a = 0
b = 1
def f(x):
    return x**2

n = 1000

x = sorted(sample(np.linspace(a, b, 5000).tolist(), n))

upper_darbu_sum = 0
lower_darbu_sum = 0

for i in range(n-1):
    x_delta = x[i+1] - x[i]
    upper_darbu_sum += max(f(x[i]), f(x[i+1]))*x_delta
    lower_darbu_sum += min(f(x[i]), f(x[i+1]))*x_delta

print('Нижняя  сумма Дарбу:', lower_darbu_sum)
print('Верхняя сумма Дарбу:', upper_darbu_sum)
