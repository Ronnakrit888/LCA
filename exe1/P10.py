if __name__ == '__main__': 
    c = float(input("Battery capacity (Wh):"))
    idle = float(input("average power (idle, mW):"))
    normal = float(input("average power (normal, mW):"))
    d_idle = c / (idle / 1000) 
    d_norm = c / (normal / 1000) 
    # Don't edit below this line.
    # ================================================================
    print('The battery will last %.0f hrs in idle mode.'%d_idle)
    print('The battery will last %.1f hrs in normal mode.'%d_norm)