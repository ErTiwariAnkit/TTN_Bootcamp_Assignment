while True:
    try:
        num = input("enetr a number")
        print(int(num))
        break
    except ValueError:
        print("try again")

