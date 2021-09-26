n=int(input())
sum_num=0
while n:
    sum_num=sum_num+n%10
    n=n//10
print(sum_num)
