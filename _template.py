# @Time    : 2020/4/18 21:42
# @Author  : gzzang
# @File    : _template
# @Project : comparison


import time
import math


def function1():
    for _ in range(n):
        a = math.pow(2, 4)


def function2():
    for _ in range(n):
        a = 2 * 2 * 2 * 2


def function3():
    for _ in range(n):
        a = 2 ** 4


function_list = [function1, function2, function3]

n = int(1e7)

for i, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{i}:{end_time - start_time}')

# 0:3.2982494831085205
# 1:0.32741808891296387
# 2:0.36425113677978516
