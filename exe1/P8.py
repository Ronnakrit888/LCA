import math

if __name__ == '__main__':
    N = int(input('Number of values:'))
    count = 0
    sum = 0
    while True:
        v = float(input("value:"))
        v = v * v
        sum += v
        count += 1
        if count == N:
            break
    rootms = math.sqrt(((1 / N ) * sum ))
    print('RMS = {:,.2f}'.format(rootms))