import random

d = random.randint(1,6)

inp = int(input("ENter a number from 1 to 6: "))

if inp > 6 or inp < 1 :
    print("not allowed!")
else:
    if d == inp :
        print("Tie")
    elif d > inp:
        print("You Lost")
    else:
        print("You won")
