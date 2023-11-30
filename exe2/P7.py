
pi = 3.141592653589793

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
    
def lastterm(k):
    if k % 2 == 0:
        return int(k//2)
    else:
        return int(k+1)//2

def taylor_sin0(x, k):
    result = 0
    for i in range(lastterm(k)):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    
    return result

def taylor_sin_halfpi(x, k):
    result = 0
    for i in range(lastterm(k)):
        result += ((-1) ** i) * ((x - pi / 2) ** (2 * i) / factorial(2 * i))

    return result

def taylor_cos0(x, k):
    result = 0
    for i in range(lastterm(k)):
        result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    
    return result

if __name__ == '__main__':
    pi = 3.141592653589793
    
    print('taylor_sin0(pi/4, 4)=', taylor_sin0(pi/4, 4))
    print('taylor_sin_halfpi(pi/4, 4)=', taylor_sin_halfpi(pi/4, 4))
    for x in [0, pi/6, pi/2, pi, pi*2]:
        print(("x = {:.2f}: sin:0,k15 = {:.4f}, " + \
            "sin:pi/2,k15 = {:.4f}").format(x, taylor_sin0(x, 15),
                                        taylor_sin_halfpi(x, 15)))
    
    print('\ntaylor_cos0(pi/4, 4)=', taylor_sin0(pi/4, 4))
    for x in [0, pi/6, pi/2, pi, pi*2]:
        print("x = {:.2f}: cos:0,k15 = {:.4f}".format(x, taylor_cos0(x, 15)))
            
