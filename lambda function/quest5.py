def odd_even(list1):
    odd = []
    even = []
    dict1 = {"odd": odd, "even": even}
    for i in list1:
        try:
            if i%2==1:
                odd.append(i)
            else:
                even.append(i)
        except TypeError:
            print("not a integer")
    print(dict1)
odd_even([23,4,6,8,"fef",76,7,76])



