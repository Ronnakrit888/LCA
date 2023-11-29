import math

def taylor_sin0(x, k):
    result = 0
    for i in range(k+1):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    
    return result

def taylor_sin_halfpi(x, k):
    result = 0
    for i in range(k+1):
        result += ((-1) ** i) * ((x - (math.pi / 2)) ** (2 * i + 1)) / math.factorial(2 * i + 1)

    return result

def taylor_cos0(x, k):
    result = 0
    for i in range(k+1):
        result += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    
    return result
