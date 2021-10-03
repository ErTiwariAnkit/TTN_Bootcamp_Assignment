num=int(input())
def pattern(num):
    return num*(num-1)
list1=list(map(pattern,range(1,num)))
print(list1)