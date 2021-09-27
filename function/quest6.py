def fun1(**kwargs):
    print(f"the number of keyword argument passed {len(kwargs)}")
    print(f"all the keys of keyword argument {kwargs.keys()}")
    print(f"all the values of keyword argument {kwargs.values()}")
fun1(a=45,b=56,c=76,d=87,e=23)