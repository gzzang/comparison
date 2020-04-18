# @Time    : 2020/4/18 21:42
# @Author  : gzzang
# @File    : loop
# @Project : comparison


import time
import numpy as np


def function1():
    for _ in range(n):
        b1 = np.zeros(m1)
        for i, v in enumerate(a):
            b1[i] = np.sqrt(v)


def function2():
    for _ in range(n):
        b2 = np.array([np.sqrt(v) for v in a])


def function3():
    ver = np.vectorize(np.sqrt)
    for _ in range(n):
        b3 = ver(a)


function_list = [function1, function2, function3]

n = int(1000)
m1 = 1000
a = np.random.rand(m1)

for i, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{i}:{end_time - start_time}')

# 0:1.9410476684570312
# 1:1.7639796733856201
# 2:1.0269076824188232
