def add(a,b,c="sum of two numbers"):
    print(c,end=" ")
    return a+b
def catch(add,*args,**kwargs):
    print(f"args {args}")
    print(f"kwargs {kwargs}")
    return add(*args,**kwargs)
print(catch(add,1,2,c="this is sum"))