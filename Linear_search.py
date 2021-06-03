# Linear search

pos = -1


def search(lst, x):
    y = 0

    for i in lst:
        if x == i:          # checking each value of the list
            globals()['pos'] = lst.index(i)  # taking the index of the element
            y = 1           # changing the flag value as found
            break           # As the element found exiting from loop
        else:
            continue        # if not found continue the loop
    if y == 1:              # checking the flag value
        return True
    else:
        return False


lst = [4, 7, 9, 2, 1, 0]

x = int(input("Enter the value:"))      # taking user input for the element we want to find

if search(lst, x):                      # calling search() for searching the element
    print("Found at position:", pos)
else:
    print("Not Found")

