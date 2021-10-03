list1=[23,56,76,8,55,86]
list2=[lambda num=num:num*105/100 for num in list1]
for i in list2:
    print(i())