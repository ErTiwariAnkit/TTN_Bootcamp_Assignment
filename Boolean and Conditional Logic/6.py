a=int(input())
b=int(input())
c=int(input())
if a==b and a==c:
    print("equilateral")
elif a!=b and b!=c and a!=c:
    print("scalene triangle")
else:
    print("isosceles")
