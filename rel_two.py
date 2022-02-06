import math as mt

def cut_frequency():
    m = input("Enter the mode you want to calculate f for frequency, c for capacitance and r for resistance: ")
    if (m == 'f'):
        c = input("Enter the capacitance value: ")
        r = input("Enter the resistance value: ")
        f = 1/(2*mt.pi*int(r)*int(c))
        print (f"f = {f} Hz")
        return f
    elif (m == 'c'):
        f = input("Enter the frequency value: ")
        r = input("Enter the resistance value: ")
        c = 1/(2*mt.pi*int(r)*int(f))
        print (f"C = {c} F")
        return c
    elif (m == 'r'):
        f = input("Enter the frequency value: ")
        c = input("Enter the capacitance value: ")
        r = 1/(2*mt.pi*int(f)*int(c))
        print (f"R = {r*pow(10,3)} kOh")
        return r
    else:
        print('Invalid Mode!')
        cut_frequency()
    
# cut_frequency()

def period ():
    f = input("Enter the frequency: ")
    t = 1/int(f)
    print(f"t = {t} s")
    return t

# print(period()/60)
