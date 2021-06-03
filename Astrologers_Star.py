'''
    i/p : integer n , boolean = True or False
    if true                 if false
    *                       ****
    **                      ***
    ***                     **
    ****                    *
'''


import sys


def pattern(n):
    b = 1
    while b:    # infinite loop for wrong i/p values continuation
        boolean = int(input("Press 1 for 'Normal' printing or Press 2 for 'Reverse' printing:"))
        if boolean == 0 or boolean < 0:     # boolean must be 1 or 2
            print("Wrong input. Try Again.")
            continue
        elif boolean > 2:                   # boolean must be 1 or 2
            print("Wrong input. Try Again.")
            continue
        else:
            if boolean == 1:        # Normal Printing
                for i in range(1, n+1):
                    print("* " * i)
                    print()
            else:                  # Reverse Printing
                for i in range(n, 0, -1):     # counting the line
                    print("* " * i)
                    print()
            break


# if __name__ == "__main__":
a = 1
while a:        # infinite loop for wrong i/p values continuation
    n = int(input("Enter the value: "))     # i/p number from user
    if n == 0 or n < 0:                     # 0 can't be an i/p
        print("Wrong input. Try Again.")
        continue
    else:
        pattern(n)          # func calling
        sys.exit()



