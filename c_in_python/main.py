import time

import my_package.c_calculate
import my_package.py_calculate

n = 10 ** 8

start = time.time()
a = my_package.c_calculate.calculate(n)
end = time.time()
print(f'c function time: {end - start}')

start = time.time()
b = my_package.py_calculate.calculate(n)
end = time.time()
print(f'python function time: {end - start}')
