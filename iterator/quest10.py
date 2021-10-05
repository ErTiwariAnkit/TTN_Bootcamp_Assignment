list1=[77,88,44,33]
def function_value(num):
    return num//11
list_map=map(function_value,list1)            #using map
for i in list_map:
    print(i)
list_compre=[i//11 for i in list1]           ##using list comprehension
print(list_compre)