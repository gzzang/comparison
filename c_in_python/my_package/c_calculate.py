import ctypes

lib_cal = ctypes.CDLL('./my_package/lib_calculate.so')


def calculate(number):
    print('c_calculate is running.')
    return lib_cal.calculate(number)
