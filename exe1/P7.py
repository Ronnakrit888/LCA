import math
def rec_to_pol(r,c):
    m = math.sqrt((r ** 2 + c ** 2))
    a = 360 + math.degrees(math.atan2(c,r))
    if a > 360:
        a -= 360
    
    return m,a

if __name__ == '__main__':  
    r, c = input('Enter (x y):').split()  
    m, a = rec_to_pol(float(r), float(c))  
    print("polar: {:.2f} with {:.2f} degree".format(m, a)) 
