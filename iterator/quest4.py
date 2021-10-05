def list_yeild(list1):
    for i in list1:
        yield i*2
list1=[2,6,7,8]
res=list_yeild(list1)
for i in res:
    print(i)