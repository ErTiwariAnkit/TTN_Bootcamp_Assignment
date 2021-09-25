list1=[1,2,3,4,5]
sum_of_even_number=0
count_even_number=0
for i in list1:
    if i%2==0:
        count_even_number=count_even_number+1
        sum_of_even_number=sum_of_even_number+i
print(f"count of even number is {count_even_number}")
print(f"sum of even number {sum_of_even_number}")
