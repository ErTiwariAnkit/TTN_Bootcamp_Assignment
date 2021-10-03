def divide(n1,n2):
    if type(n1)!=int or type(n2)!=int:
        raise Exception("this is not a whole number")
    try:
        d=n1//n2
        print(d)
    except ZeroDivisionError:
        print("can not divide by zero")
divide(24,0)
