# @Time    : 2020/4/18 21:53
# @Author  : gzzang
# @File    : range_and_arange
# @Project : comparison



import time
import numpy as np

n = int(1e4)
m = int(1e4)

def function1():
    for _ in range(n):
        t1 = [i for i in range(m)]


def function2():
    for _ in range(n):
        t2 = list(range(m))


def function3():
    for _ in range(n):
        t3 = np.arange(m)


function_list = [function1, function2, function3]



for i, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{i}:{end_time - start_time}')