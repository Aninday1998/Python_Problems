''' Snake-Water-Gun problem('S' for Snake, 'W' for Water, 'G' for Game)
    User           CPU            Winner
     S              W       =       S
     S              G       =       G
     W              G       =       W
     W              S       =       S
     G              S       =       G
     G              W       =       G
else draw.
Play 10 times and show who is the winner.   '''

import random
import sys


def r_fun():            # random of snake, water and gun
    lst = ['s', 'w', 'g']
    return random.choice(lst)


def game_compare(n1):

    ''' This method shows the winner for each round and returns the counter values for final total results. '''

    m, c, dw = 0, 0, 0       # m = human win count, c = cpu win count, dw = draw count
    d = r_fun()
    if n1 == 's' and d == 'w':              # human wins
        m += 1                              # increasing Human counter
        n1, d = 'Snake', 'Water'
        print("You = {} , CPU = {}\n!! Congo !! You Win.\n".format(n1, d))
    elif n1 == 's' and d == 'g':            # cpu wins
        c += 1                              # increasing cpu counter
        n1, d = 'Snake', 'Gun'
        print("You = {} , CPU = {}\nOOPs !! You Loose.\n".format(n1, d))
    elif n1 == 'w' and d == 'g':            # human wins
        m += 1                              # increasing Human counter
        n1, d = 'Water', 'Gun'
        print("You = {} , CPU = {}\nCongo !! You Win.\n".format(n1, d))
    elif n1 == 'w' and d == 's':            # cpu wins
        c += 1                              # increasing cpu counter
        n1, d = 'Water', 'Snake'
        print("You = {} , CPU = {}\nOOPs !! You Loose.\n".format(n1, d))
    elif n1 == 'g' and d == 's':          # Human wins
        m += 1                            # increasing Human counter
        n1, d = 'Gun', 'Snake'
        print("You = {} , CPU = {}\nCongo !! You Win.\n".format(n1, d))
    elif n1 == 'g' and d == 'w':        # cpu wins
        c += 1                          # increasing cpu counter
        n1, d = 'Gun', 'Water'
        print("You = {} , CPU = {}\nOOPs !! You Loose.\n".format(n1, d))
    elif n1 == d:                           # draw
        if n1 == 's':
            n1, d = 'Snake', 'Snake'
        elif n1 == 'w':
            n1, d = 'Water', 'Water'
        elif n1 == 'g':
            n1, d = 'Gun', 'Gun'
        dw += 1                         # increasing draw counter
        print("You = {} , CPU = {}\n!! Match draw !!\n".format(n1, d))
    else:
        print("Something Wrong")

    return m, c, d          # m = human win count, c = cpu win count, dw = draw count


def start_game():

    ''' This method takes i/p from user and calculates the final result '''

    j = 1
    a = int(input("Enter how many times you want to play:"))
    while j < a + 1:
        n = input("Press 's' for Snake, 'w' for Water, 'g' for Gun and for EXIT press 2:\n")
        # n1 = n.capitalize()
        x, y, z = 0, 0, 0
        if n == 's' or n == 'w' or n == 'g':
            m, c, dw = game_compare(n)           # m = human win count, c = cpu win count, dw = draw count
        elif n == '2':
            sys.exit("Thank You")
        else:
            print("!!!  Wrong Input  !!! Try Again.")
            continue
        j += 1
    if m > c:                           # Human count is more
        print("Final Result: !!!  You win  !!!\n")
    elif m < c:                         # Cpu count is more
        print("Final Result: !!!  Sorry You loose  !!!\n")
    elif m == c:                        # Equal number of count
        print("Final Result: !!!  Match Draw !!!\n")


        # Play for First time
n = int(input("!!!       Welcome to Snake-Water-Gun Game      !!!\nPress 1 to Play or Press 2 to Exit:\n"))
if n == 1:
    start_game()
else:
    sys.exit("Thank You")

# print("Thank you")

        # Play for multiple times
a = 1
while a:        # infinite loop
    n = int(input("Press 1 to play Again or Press 2 to Exit"))
    if n == 1:
        start_game()
    else:
        sys.exit("Thank You")
print("Thank you")
