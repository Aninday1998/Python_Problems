''' You have 5 chances to guess a number that is defined in the system.
    i/p : You have to take the number every time which will be equal to that target number
    o/p : if found print "won the game" and also in the no. of chances you need. else you have to print "SRY . Failed"
'''

import random           # for set setting a random target number


# global variables
f = -1      # flag for getting the number
c = 0       # Counter for the number of chances left(does not count the wrong i/p in-between the number search)


def guess(x, ch):       # guess() takes 2 arg. x is target no. ch is number of chances.

    l, u = 0, 100      # lower value & upper value of the game
    for i in range(1, 500):     # loop will execute for 5 times
        globals()['c'] += 1     # c = counter . if we give wrong i/p in-between the no of searches.
        n = int(input("Enter the Number between 0 to 100:\n"))     # user i/p the number
        if n <= 100:       # i/p range check
            if x == n:        # if element found
                globals()['f'] = 1      # changing the flag value as found the number
                ch1 = c                # set how many chances are left
                break
            elif n > x:
                mid = n - x         # finding how much ahead the number is from the target number
                if ch == 1:         # no chances left
                    print("!!! SRY !!! You lost .")
                    break
                else:               # if chances left
                    print("!! OPS !! You are {} ahead of the Number.".format(mid))
                    print("!! Be Quick !! You have {} chances left\n".format(ch - 1))
            else:
                mid = x - n     # finding how much below the number is from the target number
                if ch == 1:     # no chances left
                    print("!!! SRY !!! You lost .")
                    break
                else:           # if chances left
                    print("!! OPS !! You are {} below of the Number.".format(mid))
                    print("!! Be Quick !! You have {} chances left\n".format(ch - 1))

            ch -= 1             # decreasing the chances

        else:
            print("!!! Wrong i/p !!!")          # if the i/p is out of the range
            continue
    if f == 1:                  # As the flag value matches, we found the number.
        print("!!!! Congratulations !!!! You found the Number at {} chance.".format(ch1 - 2))




x = random.randint(1,100)      # Target Number
ch = 5      # 5 guesses by default
lst = guess(x, ch)          # calling the method
