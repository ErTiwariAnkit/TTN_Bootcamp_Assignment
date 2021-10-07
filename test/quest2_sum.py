def sum_fun(n):
    sum1=0
    while n:
        sum1=sum1+n%10
        n=n//10
    return sum1