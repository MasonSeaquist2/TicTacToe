# VARS
sqr1 = " 1 "
sqr2 = " 2 "
sqr3 = " 3 "
sqr4 = " 4 "
sqr5 = " 5 "
sqr6 = " 6 "
sqr7 = " 7 "
sqr8 = " 8 "
sqr9 = " 9 "
game_over = False
turns = 9


def board():
    print(" ___ ___ ___")
    print("|" + sqr1 + "|" + sqr2 + "|" + sqr3 + "|")
    print(" ___ ___ ___")
    print("|" + sqr4 + "|" + sqr5 + "|" + sqr6 + "|")
    print(" ___ ___ ___")
    print("|" + sqr7 + "|" + sqr8 + "|" + sqr9 + "|")
    print(" ___ ___ ___")


def xmove():
    global sqr1
    global sqr2
    global sqr3
    global sqr4
    global sqr5
    global sqr6
    global sqr7
    global sqr8
    global sqr9
    board()
    move = input("What square X? ")
    if move == "1" and sqr1 == " 1 ":
        sqr1 = " X "
        return True
    elif move == "2" and sqr2 == " 2 ":
        sqr2 = " X "
        return True
    elif move == "3" and sqr3 == " 3 ":
        sqr3 = " X "
        return True
    elif move == "4" and sqr4 == " 4 ":
        sqr4 = " X "
        return True
    elif move == "5" and sqr5 == " 5 ":
        sqr5 = " X "
        return True
    elif move == "6" and sqr6 == " 6 ":
        sqr6 = " X "
        return True
    elif move == "7" and sqr7 == " 7 ":
        sqr7 = " X "
        return True
    elif move == "8" and sqr8 == " 8 ":
        sqr8 = " X "
        return True
    elif move == "9" and sqr9 == " 9 ":
        sqr9 = " X "
        return True
    else:
        return False


def omove():
    global sqr1
    global sqr2
    global sqr3
    global sqr4
    global sqr5
    global sqr6
    global sqr7
    global sqr8
    global sqr9
    board()
    move = input("What square O? ")
    if move == "1" and sqr1 == " 1 ":
        sqr1 = " O "
        return True
    elif move == "2" and sqr2 == " 2 ":
        sqr2 = " O "
        return True
    elif move == "3" and sqr3 == " 3 ":
        sqr3 = " O "
        return True
    elif move == "4" and sqr4 == " 4 ":
        sqr4 = " O "
        return True
    elif move == "5" and sqr5 == " 5 ":
        sqr5 = " O "
        return True
    elif move == "6" and sqr6 == " 6 ":
        sqr6 = " O "
        return True
    elif move == "7" and sqr7 == " 7 ":
        sqr7 = " O "
        return True
    elif move == "8" and sqr8 == " 8 ":
        sqr8 = " O "
        return True
    elif move == "9" and sqr9 == " 9 ":
        sqr9 = " O "
        return True
    else:
        return False


def checkwinx():
    if sqr1 == " X " and sqr2 == " X " and sqr3 == " X ":
        return True
    if sqr4 == " X " and sqr5 == " X " and sqr6 == " X ":
        return True
    if sqr7 == " X " and sqr8 == " X " and sqr9 == " X ":
        return True
    if sqr1 == " X " and sqr4 == " X " and sqr7 == " X ":
        return True
    if sqr2 == " X " and sqr5 == " X " and sqr8 == " X ":
        return True
    if sqr3 == " X " and sqr6 == " X " and sqr9 == " X ":
        return True
    if sqr1 == " X " and sqr5 == " X " and sqr9 == " X ":
        return True
    if sqr3 == " X " and sqr5 == " X " and sqr7 == " X ":
        return True


def checkwino():
    if sqr1 == " O " and sqr2 == " O " and sqr3 == " O ":
        return True
    if sqr4 == " O " and sqr5 == " O " and sqr6 == " O ":
        return True
    if sqr7 == " O " and sqr8 == " O " and sqr9 == " O ":
        return True
    if sqr1 == " O " and sqr4 == " O " and sqr7 == " O ":
        return True
    if sqr2 == " O " and sqr5 == " O " and sqr8 == " O ":
        return True
    if sqr3 == " O " and sqr6 == " O " and sqr9 == " O ":
        return True
    if sqr1 == " O " and sqr5 == " O " and sqr9 == " O ":
        return True
    if sqr3 == " O " and sqr5 == " O " and sqr7 == " O ":
        return True


while not game_over:
    while not xmove():
        print("not a valid move")
    if checkwinx():
        board()
        print("X Wins!")
        break
    turns -= 1
    if turns < 1:
        board()
        print("Its a tie!")
        break
    while not omove():
        print("Not a valid move")
    if checkwino():
        board()
        print("O Wins!")
        break
    turns -= 1
    if turns < 1:
        board()
        print("Its a tie!")
        break
