# @Time    : 2020/4/18 21:56
# @Author  : gzzang
# @File    : array_multiplication
# @Project : comparison


import time
import numpy as np

n = int(1e4)
m1 = 50
m2 = 30

a = np.random.rand(m1, m2)
b = np.random.rand(1, m2)


def function1():
    for _ in range(n):
        c = a * b


def function2():
    for _ in range(n):
        c = np.zeros_like(a)
        for j in range(m1):
            c[j, :] = a[j, :] * b


def function3():
    for _ in range(n):
        c = np.array([v * b for v in a])


function_list = [function1, function2, function3]

for i, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{i}:{end_time - start_time}')

# 0:0.03992152214050293
# 1:1.5278959274291992
# 2:1.322563648223877
