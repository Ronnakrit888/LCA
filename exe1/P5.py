def power_equiv(watt):  
    hp = watt * 0.00134 
    btum = watt * 3.41297  
    calm = watt * 14.33  
    erg = watt * 10000000  
    flbm = watt * 44.25  
    return hp, btum, calm, erg, flbm  
if __name__ == '__main__':  
    pwatt = 100  
    horsep, btuh, calmin, perg, footlbm = power_equiv(pwatt)  
    print(pwatt, 'w =', round(horsep,3), 'hp =',  
    round(btuh,3), 'btu/h =',  
    round(calmin,3),'cal/min =',  
    round(perg,3), 'erg =',  
    round(footlbm,3), 'f-lb/min')


