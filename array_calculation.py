# @Time    : 2020/4/21 20:40
# @Author  : gzzang
# @File    : array_calculation
# @Project : comparison


import time
import numpy as np

import pdb

n = int(1e2)

m = 100
x = np.random.rand(m, 2)


# # y = x.repeat(repeats=[4],axis=1)
# y = x.reshape([m,1,2]).repeat(repeats=4,axis=1)
# print(y[:,:,0])
# print(y.shape)
# y2 = x.reshape([1,m,2]).repeat(repeats=4,axis=0)
# print(y2[:,:,0])
# print(y2.shape)
# z = y2-y
# print(z[:,:,0])
# print(z.shape)
# # z2 = np.linalg.norm(x=z,ord=2,axis=2)
# z2 = np.linalg.norm(x=x.reshape([m,1,2]).repeat(repeats=4,axis=1) - x.reshape([1,m,2]).repeat(repeats=4,axis=0),ord=2,axis=2)
# print(z2)
# print(z2.shape)
# pdb.set_trace()


def function1():
    for _ in range(n):
        a = np.array([[np.linalg.norm(v1 - v2, ord=2) for v1 in x] for v2 in x])
    return a


def function2():
    for _ in range(n):
        a = np.linalg.norm(
            x=x.reshape([m, 1, 2]).repeat(repeats=m, axis=1) - x.reshape([1, m, 2]).repeat(repeats=m, axis=0),
            ord=2,
            axis=2)
    return a


def function3():
    for _ in range(n):
        a = 2 ** 4
    return a


function_list = [function1, function2]

for i, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{i}:{end_time - start_time}')

# 0:1.5688252449035645
# 1:0.02894115447998047
# 2:0.03585624694824219
