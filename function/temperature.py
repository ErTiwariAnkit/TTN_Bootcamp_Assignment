def convert_cel_to_far(C):
    F=C*9/5+32
    return F
def convert_far_to_cel(F):
    C=(F-32)*5/9
    return C
f=float(input("enter a temperature in degrees fahrenheit"))
print(f"{f} degrees F={convert_far_to_cel(f):.2f} degrees C")
c=float(input("enter a temperature in degrees celsius"))
print(f"{c} degrees C={convert_cel_to_far(c):.2f} degrees F")