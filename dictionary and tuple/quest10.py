d1 = {'1': 1, '2': 2, '3': 3}
d2 = {'4': 4, '5': 5, '6': 6}
d3=d1
def merge(d1,d2):
    return d3.update(d2)
merge(d1,d2)
print(d3)