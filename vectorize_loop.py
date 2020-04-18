# @Time    : 2020/4/18 21:47
# @Author  : gzzang
# @File    : vectorize_loop
# @Project : comparison


import time
import numpy as np


def function1():
    for _ in range(n):
        b1 = np.zeros(m1)
        for i, v in enumerate(a):
            b1[i] = v.sum()


def function2():
    for _ in range(n):
        b2 = [v.sum() for v in a]


def function3():
    ver = np.vectorize(np.sum, signature='(n)->()')
    for _ in range(n):
        b3 = ver(a)


function_list = [function1, function2, function3]

n = int(1e1)

m1 = 100000
m2 = 100

a = np.random.rand(m1, m2)

for i, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{i}:{end_time - start_time}')

# 0:2.9971985816955566
# 1:2.8196446895599365
# 2:7.73806357383728
