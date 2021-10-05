def decor_greet(greet1):
    def space_underscore():
        t2=""
        for i in greet1():
            if i==" ":
                t2=t2+"_"
            else:
                t2=t2+i
        return t2
    return space_underscore
def decor_greetfun(greet1):
        def capital_letters():
            return greet1().upper()
        return capital_letters
@decor_greet
def greet():
    return 'Welcome to Python'
print(greet())
@decor_greetfun
def greet():
    return 'Welcome to Python'
print(greet())