data_pair=int(input("Enter number of data pair"))
while(data_pair):
    A=input("player A move")
    B=input("player B move")
    if A=="R":
        if B=="P":
            print("B WINS")
        elif B=="S":
            print("A WINS")
        else:
            print("DRAW")
    if A=="P":
        if B=="R":
            print("A WINS")
        elif B=="S":
            print("B WINS")
        else:
            print("DRAW")
    if A=="S":
        if B=="P":
            print("A WINS")
        elif B=="R":
            print("B WINS")
        else:
            print("DRAW")
    data_pair=data_pair-1
