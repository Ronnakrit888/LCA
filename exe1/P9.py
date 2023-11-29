a = int(input("Battery capacity (mAh):"))
e = format((a / 1000) * 12,".2f")
print("At its 12 V rating, it stores",e,"Wh.")