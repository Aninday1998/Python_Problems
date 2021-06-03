
pos = -1                # suppose the position of the element is -1

def search(list, x):       # calling the search method

    l = 0       # lower bound of the list
    u = len(lst) + 1    # upper bound of the list

    for i in range(l, u + 1):       # loop goes from lower bound to upper bound
        mid = int((l + u) / 2)      # finding the mid position

        if x == mid:        # for succesful search
            globals()['pos'] = mid
            return pos
        elif mid < x:       # if the element is bigger than the value at mid
            l = mid + 1
        else:               # if the element is smaller than the value at mid
            u = mid - 1


lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]       # taking the list

list = lst.sort()               # sorting the list

x = 5                           # the element we want to find

if search(list, x):             # calling search method
    print("Found at position:",lst[-pos] )
else:
    print("Not Found")