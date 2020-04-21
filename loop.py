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
    return b1


def function2():
    for _ in range(n):
        b2 = np.array([np.sqrt(v) for v in a])
    return b2


def function3():
    ver = np.vectorize(np.sqrt)
    for _ in range(n):
        b3 = ver(a)
    return b3


def function4():
    for _ in range(n):
        b4 = np.sqrt(a)
    return b4


function_list = [function1, function2, function3, function4]

n = int(1000)
m1 = 1000
a = np.random.rand(m1)

for i, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{i}:{end_time - start_time}')

# 0:2.0077333450317383
# 1:1.8613100051879883
# 2:0.9722146987915039
# 3:0.001993894577026367
