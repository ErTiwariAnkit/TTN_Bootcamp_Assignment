d1 = {'1': 1, '2': 2, '3': 3}
d2 = {'4': 4, '5': 5, '6': 6}
d3=d1
def merge(d1,d2):
    d3.update(d2)
def merge1(d1,d2):
    result=d1|d2
    return result
merge(d1,d2)
dict1=merge1(d1,d2)
print(dict1)
print(d3)