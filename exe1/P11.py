e = int(input("Energy( in kcal):"))
joules = e * 4184
print("That is",format(joules,".2f"),"J or",round(joules / 3600,2),"Wh.")