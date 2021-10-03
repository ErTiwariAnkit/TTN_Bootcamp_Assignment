list1=[44,55,6,3,5,19,23,29,86]
def is_prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return num>1
def prime_filt(list1):
    return list(filter(is_prime,list1))
print(prime_filt(list1))