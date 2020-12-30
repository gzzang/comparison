# @time: 2020/12/30 10:18
# @author: gzzang
# @file: numpy_matrix.py
# @project: comparison_note

import time
import numpy as np


def function1():
    for _ in range(n):
        it = (i * np.eye(N=m1, k=i, dtype=int) for i in range(1, m1 + 1))
        b1 = sum(it)
    return b1


def function2():
    for _ in range(n):
        b2 = np.zeros(shape=[m1, m1], dtype=int)
        for i in range(1, m1 + 1):
            b2 += i * np.eye(N=m1, k=i, dtype=int)
    return b2


def function3():
    for _ in range(n):
        b3 = np.zeros(shape=[m1, m1], dtype=int)
        for i in range(1, m1):
            for j in range(m1 - i):
                b3[j, j + i] = i
    return b3


function_list = [function1, function2, function3]

n = int(1)
m1 = 500

for ii, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{ii}:{end_time - start_time}')

# 0:0.5370464324951172
# 1:0.3959846496582031
# 2:0.017927885055541992
