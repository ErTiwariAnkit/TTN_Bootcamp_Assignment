import random
roll_list1=list(map(lambda  x:random.randint(1,6),range(10000)))
print(sum(roll_list1)//10000)