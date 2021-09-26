#ceil function
def ceil(x):
    if x==int(x):
        return int(x)
    return int(x+1)
print("ceil")
print(ceil(3.0))
print(ceil(-5.5))
#floor function
def floor(x):
    if(x>=0):
        return int(x)
    else:
        return int(x-1)
print("floor")
print(floor(-3.6))
