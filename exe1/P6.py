a = int(input("a: "))
b = int(input("b: "))

if a == 0 and b > 0:
    print("a/b =",float(a/b))
elif b == 0:
    if a > 0:
        print("a/b = Infinity")
    elif a < 0:
        print("a/b = Negative infinity")
    else:
       print("a/b = Not defined") 
else:
    print("a/b =",round(float(a/b),1))
