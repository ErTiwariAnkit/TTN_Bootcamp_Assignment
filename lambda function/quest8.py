try:
    num=int(input("enter a number"))
    str1=input("enter a string")
    print(str1[num])
except ValueError:
    print("index is not a integer")
except IndexError:
    print("index is out of range try with another index")