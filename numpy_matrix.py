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


def function4():
    for _ in range(n):
        b4 = np.triu(np.reshape(np.tile(np.arange(m1), m1) - np.repeat(np.arange(m1), m1), (m1, m1)))
    return b4


function_list = [function1, function2, function3, function4]

n = int(1)
m1 = 500

for ii, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{ii}:{end_time - start_time}')

# 0:0.3749988079071045
# 1:0.3709754943847656
# 2:0.015956878662109375
# 3:0.001995086669921875
