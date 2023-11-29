v = float(input("Enter voltage (V): "))
a = float(input("Enter current (A): "))
t = int(input("Enter operating time (h): "))
unit = (v * a * t) / 1000
print("The cost is",unit * 4)