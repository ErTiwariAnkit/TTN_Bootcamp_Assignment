def isiterable(object1):
    try:
        iter(object1)
        print(f"object {object1} is iterable")
    except TypeError:
        print(f"objec {object1} is not iterable")
list1=[23,435,68,87]
isiterable(list1)