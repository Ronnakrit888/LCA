def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return (num * factorial(num - 1))




# factorial 5 = 5 x 4 x 3 x 2 x 1