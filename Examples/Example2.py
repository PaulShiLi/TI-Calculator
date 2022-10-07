import basic.calc
from basic import calc
# Rock = 0
# Paper = 1
# Scissors = 2

W = 0
L = 0
T = 0

while 0==0:
    print("Choose:")
    print("Rock: 0")
    print("Paper: 1")
    print("Scissors: 2")
    A = int(input("Choose: "))
    B = calc.Prb.randint(0, 2)
    calc.clear()
    if B == 0:
        print("Calc chose:")
        print("Rock")
    if B == 1:
        print("Calc chose:")
        print("Paper")
    if B == 2:
        print("Calc chose:")
        print("Scissors")
    if A > 2:
        print("Please put")
        print("a valid Num!")
    if A == B:
        T += 1
        print("Its a tie!")
    if B == 0:
        if A == 1:
            W += 1
            print("You Win!")
        if A == 2:
            L += 1
            print("You Lost!")
    if B == 1:
        if A == 2:
            W += 1
            print("You Win!")
        if A == 0:
            L += 1
            print("You Lost!")
    if B == 2:
        if A == 0:
            W += 1
            print("You Win!")
        if A == 1:
            L += 1
            print("You Lost!")
    print("Press any number")
    input("to move on")
    calc.clear()
    print("Your Score:")
    print("Wins: ",W)
    print("Losses: ", L)
    print("Ties: ", T)
    print("Again?:")
    print("Yes: 0")
    print("No: 1")
    D = int(input("> "))
    if D == 1:
        break