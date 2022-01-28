import math as mt

def equivalent_resistor(*r_args):
    rm,rp = 1,0
    if len(r_args) <= 0:
        return
    for c in r_args:
        rm *= c
        rp += c
    req = rm/rp
    return req

def current_divisor(i, rx, *r_args):
    rm,rp = 1,0
    if len(r_args) <= 0:
        return
    for c in r_args:
        rm *= c
        rp += c
    req = rm/rp
    return (i*req/(rx+req))

I_1 = 0.80*mt.pow(10,-3)
R_1 = 0.5*mt.pow(10,3)
R_2 = 72*mt.pow(10,3)
R_3 = 0.4*mt.pow(10,3)
V = equivalent_resistor(equivalent_resistor(R_1, R_2), R_3) * I_1

I_r1 = current_divisor(I_1, R_1, R_2, R_3)
I_r2 = current_divisor(I_1, R_2, R_1, R_3)
I_r3 = current_divisor(I_1, R_3, R_2, R_1) 

I_tot = I_r1 + I_r2 + I_r3
P_r1 = mt.pow(I_r1,2) * R_1
P_r2 = mt.pow(I_r2,2) * R_2
P_r3 = mt.pow(I_r3,2) * R_3
P_tot = P_r1 + P_r2 + P_r3

print(f"V = {V} V")
print (f"Ir1 = {I_r1} A")
print (f"Ir2 = {I_r2} A")
print (f"Ir3 = {I_r3} A")
print (f"I_total = {I_tot} A")

print (f"P_r1 = {P_r1} W")
print (f"P_r2 = {P_r2} W")
print (f"P_r3 = {P_r3} W")
print (f"P_tot = {P_tot} W")
