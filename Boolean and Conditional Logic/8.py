import random
number=random.randrange(1,50)
guessCheck="wrong"
print("Welcome to Number Guess")

while guessCheck=="wrong":
    
    res=int(input("Please input a number between 1 and 50:"))
    if res!=number:
        print("This is not a valid integer. Please try again")
    if res<number:
        print("This is lower than actual number. Please try again.")
    elif res>number:
        print("This is higher than actual number. Please try again.")
    else:
        print("This is the correct number")
        guessCheck="correct"
