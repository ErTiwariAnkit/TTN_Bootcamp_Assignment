def convert_cel_to_far(C):
    F=C*9/5+32
    return float((f"{F:,.2f}"))
def convert_far_to_cel(F):
    C=(F-32)*5/9
    return float((f"{C:,.2f}"))
print(convert_cel_to_far(37))
print(convert_far_to_cel(72))