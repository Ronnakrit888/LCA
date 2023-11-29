import math
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

def taylor_exp0(x, k):
    result = 1

    for i in range(1, k+1):
        result += (x ** i) / factorial(i)

    return result
