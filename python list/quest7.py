import time
begin = time.time()
#for loop
list1=[]
for i in range (1,1000001):
    list1.append(i)
#list comprehension
list2=[i for i in range(1000001)]
time.sleep(1)
end = time.time()
print(f"Total runtime of the program is {end - begin}")
