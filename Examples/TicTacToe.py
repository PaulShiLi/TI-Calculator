import os

L1 = []
for N in range(10):
    L1.append(3)

print("Board:")
print("|1|2|3|")
print("|4|5|6|")
print("|7|8|9|")
print("Press 0 to continue:")
input()
os.system("clear")

while 1 == 1:
    # Print Board
    str1 = "|"
    str2 = "|"
    str3 = "|"
    if L1[0] == 0:
        str1 = str1 + "0|"
    if L1[0] == 1:
        str1 = str1 + "X|"
    if L1[0] != 0 and L1[0] != 1:
        str1 = str1 + " |"

    if L1[1] == 0:
        str1 = str1 + "0|"
    if L1[1] == 1:
        str1 = str1 + "X|"
    if L1[1] != 0 and L1[1] != 1:
        str1 = str1 + " |"

    if L1[2] == 0:
        str1 = str1 + "0|"
    if L1[2] == 1:
        str1 = str1 + "X|"
    if L1[2] != 0 and L1[2] != 1:
        str1 = str1 + " |"
    #
    if L1[3] == 0:
        str2 = str2 + "0|"
    if L1[3] == 1:
        str2 = str2 + "X|"
    if L1[3] != 0 and L1[3] != 1:
        str2 = str2 + " |"

    if L1[4] == 0:
        str2 = str2 + "0|"
    if L1[4] == 1:
        str2 = str2 + "X|"
    if L1[4] != 0 and L1[4] != 1:
        str2 = str2 + " |"

    if L1[5] == 0:
        str2 = str2 + "0|"
    if L1[5] == 1:
        str2 = str2 + "X|"
    if L1[5] != 0 and L1[5] != 1:
        str2 = str2 + " |"
    #
    if L1[6] == 0:
        str3 = str3 + "0|"
    if L1[6] == 1:
        str3 = str3 + "X|"
    if L1[6] != 0 and L1[6] != 1:
        str3 = str3 + " |"

    if L1[7] == 0:
        str3 = str3 + "0|"
    if L1[7] == 1:
        str3 = str3 + "X|"
    if L1[7] != 0 and L1[7] != 1:
        str3 = str3 + " |"

    if L1[8] == 0:
        str3 = str3 + "0|"
    if L1[8] == 1:
        str3 = str3 + "X|"
    if L1[8] != 0 and L1[8] != 1:
        str3 = str3 + " |"
    print(str1)
    print(str2)
    print(str3)
    ###
    A = int(input("Turn [O]: "))
    if L1[A - 1] != 0 and L1[A - 1] != 1:
        L1[A - 1] = 0
    else:
        print("Spot has")
        print("taken!")
        A = int(input("Turn [O]: "))
        L1[A - 1] = 0
    os.system("clear")
    if L1[0] == 0 and L1[1] == 0 and L1[2] == 0:
        print("[0] Won!")
        break
    if L1[0] == 1 and L1[1] == 1 and L1[2] == 1:
        print("[X] Won!")
        break
    if L1[0] == 0 and L1[3] == 0 and L1[6] == 0:
        print("[0] Won!")
        break
    if L1[0] == 1 and L1[3] == 1 and L1[6] == 1:
        print("[X] Won!")
        break
    if L1[6] == 0 and L1[7] == 0 and L1[8] == 0:
        print("[0] Won!")
        break
    if L1[6] == 1 and L1[7] == 1 and L1[8] == 1:
        print("[X] Won!")
        break
    if L1[2] == 0 and L1[5] == 0 and L1[8] == 0:
        print("[0] Won!")
        break
    if L1[2] == 1 and L1[5] == 1 and L1[8] == 1:
        print("[X] Won!")
        break
    if L1[1] == 0 and L1[4] == 0 and L1[7] == 0:
        print("[0] Won!")
        break
    if L1[1] == 1 and L1[4] == 1 and L1[7] == 1:
        print("[X] Won!")
        break
    if L1[3] == 0 and L1[4] == 0 and L1[5] == 0:
        print("[0] Won!")
        break
    if L1[3] == 1 and L1[4] == 1 and L1[5] == 1:
        print("[X] Won!")
        break
    if L1[0] == 0 and L1[4] == 0 and L1[8] == 0:
        print("[0] Won!")
        break
    if L1[0] == 1 and L1[4] == 1 and L1[8] == 1:
        print("[X] Won!")
        break
    if L1[2] == 0 and L1[4] == 0 and L1[6] == 0:
        print("[0] Won!")
        break
    if L1[2] == 1 and L1[4] == 1 and L1[6] == 1:
        print("[X] Won!")
        break
    Z = 0
    N = 0
    for N in range(len(L1)):
        if L1[N] == 0 or L1[N] == 1:
            Z += 1
    if Z == len(L1):
        print("Its a tie!")
        break
    # Print Board
    str1 = "|"
    str2 = "|"
    str3 = "|"
    if L1[0] == 0:
        str1 = str1 + "0|"
    if L1[0] == 1:
        str1 = str1 + "X|"
    if L1[0] != 0 and L1[0] != 1:
        str1 = str1 + " |"

    if L1[1] == 0:
        str1 = str1 + "0|"
    if L1[1] == 1:
        str1 = str1 + "X|"
    if L1[1] != 0 and L1[1] != 1:
        str1 = str1 + " |"

    if L1[2] == 0:
        str1 = str1 + "0|"
    if L1[2] == 1:
        str1 = str1 + "X|"
    if L1[2] != 0 and L1[2] != 1:
        str1 = str1 + " |"
    #
    if L1[3] == 0:
        str2 = str2 + "0|"
    if L1[3] == 1:
        str2 = str2 + "X|"
    if L1[3] != 0 and L1[3] != 1:
        str2 = str2 + " |"

    if L1[4] == 0:
        str2 = str2 + "0|"
    if L1[4] == 1:
        str2 = str2 + "X|"
    if L1[4] != 0 and L1[4] != 1:
        str2 = str2 + " |"

    if L1[5] == 0:
        str2 = str2 + "0|"
    if L1[5] == 1:
        str2 = str2 + "X|"
    if L1[5] != 0 and L1[5] != 1:
        str2 = str2 + " |"
    #
    if L1[6] == 0:
        str3 = str3 + "0|"
    if L1[6] == 1:
        str3 = str3 + "X|"
    if L1[6] != 0 and L1[6] != 1:
        str3 = str3 + " |"

    if L1[7] == 0:
        str3 = str3 + "0|"
    if L1[7] == 1:
        str3 = str3 + "X|"
    if L1[7] != 0 and L1[7] != 1:
        str3 = str3 + " |"

    if L1[8] == 0:
        str3 = str3 + "0|"
    if L1[8] == 1:
        str3 = str3 + "X|"
    if L1[8] != 0 and L1[8] != 1:
        str3 = str3 + " |"
    print(str1)
    print(str2)
    print(str3)
    ###
    B = int(input("Turn [X]: "))
    if L1[B - 1] != 0 and L1[B - 1] != 1:
        L1[B - 1] = 1
    else:
        print("Spot has")
        print("taken!")
        B = int(input("Turn [X]: "))
        L1[B - 1] = 1
    os.system("clear")
    if L1[0] == 0 and L1[1] == 0 and L1[2] == 0:
        print("[0] Won!")
        break
    if L1[0] == 1 and L1[1] == 1 and L1[2] == 1:
        print("[X] Won!")
        break
    if L1[0] == 0 and L1[3] == 0 and L1[6] == 0:
        print("[0] Won!")
        break
    if L1[0] == 1 and L1[3] == 1 and L1[6] == 1:
        print("[X] Won!")
        break
    if L1[6] == 0 and L1[7] == 0 and L1[8] == 0:
        print("[0] Won!")
        break
    if L1[6] == 1 and L1[7] == 1 and L1[8] == 1:
        print("[X] Won!")
        break
    if L1[2] == 0 and L1[5] == 0 and L1[8] == 0:
        print("[0] Won!")
        break
    if L1[2] == 1 and L1[5] == 1 and L1[8] == 1:
        print("[X] Won!")
        break
    if L1[1] == 0 and L1[4] == 0 and L1[7] == 0:
        print("[0] Won!")
        break
    if L1[1] == 1 and L1[4] == 1 and L1[7] == 1:
        print("[X] Won!")
        break
    if L1[3] == 0 and L1[4] == 0 and L1[5] == 0:
        print("[0] Won!")
        break
    if L1[3] == 1 and L1[4] == 1 and L1[5] == 1:
        print("[X] Won!")
        break
    if L1[0] == 0 and L1[4] == 0 and L1[8] == 0:
        print("[0] Won!")
        break
    if L1[0] == 1 and L1[4] == 1 and L1[8] == 1:
        print("[X] Won!")
        break
    if L1[2] == 0 and L1[4] == 0 and L1[6] == 0:
        print("[0] Won!")
        break
    if L1[2] == 1 and L1[4] == 1 and L1[6] == 1:
        print("[X] Won!")
        break
    Z = 0
    N = 0
    for N in range(len(L1)):
        if L1[N] == 0 or L1[N] == 1:
            Z += 1
    if Z == len(L1):
        print("Its a tie!")
        break