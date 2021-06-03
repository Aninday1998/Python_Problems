'''
    Health Management System:
     3 clients: Harry, Rohan, Hamad. create 3 files for their exercise & 3 files for their diet .
     op: you can change or read the file . all the files must include the current times
     use the func for time :
     def getData():
     import datetime
     return datetime.datetime.now()
'''

import sys
import datetime


def getTime():
    ''' This Function returns the date & time'''
    return datetime.datetime.now()


def diet(n):
    ''' This function makes files for creating diet chart of 3 people on everyday basis'''
    # with open("Harry_Diet", 'w') as ha:  # Harry's Diet
    #     ha.write("\n!! Harry's Diet !!\nBreakfast: Oats, Milk\n\nLunch: Rice, Dal, Sabzi\n\nDinner: Roti, Sabzi, Milk")
    #
    # with open("Rohan_Diet", 'w') as r:  # Rohan's Diet
    #     r.write("\n!! Rohan's Diet !!\nBreakfast: Roti, Sabzi\n\nLunch: Rice, Fish, Salad\n\nDinner: Rice, Dal, Sabzi")
    #
    # with open("Hamad_Diet", 'w') as h:  # Hamad's Diet
    #     h.write("\n!! Hamad's Diet !!\nBreakfast: Oats, Dry fruits, Milk\n\nLunch: Rice, Dal, Paneer, Salad, Curd\n\nDinner: Oats, Milk\n")

    t1 = getTime()          # for fetching time and date from system

    n1 = int(input("\nPress 1 to See the Diet Chart or Press 2 to Change the Diet Chart:\n"))

    # Read Only Mode for Diet Chart

    if n1 == 1:
        n2 = int(input("Press 1 for Harry's Diet, Press 2 for Rohan's Diet, Press 3 for Hamad's Diet:\n"))

        # Harry's Diet
        if n2 == 1:
            t1 = getTime()                  # Calling the getTime() for Date & Time
            with open("Harry_Diet", 'r') as f:  # opening Harry's Diet in read mode
                print(t1, "\n", f.read())       # printing Harry's diet

        # Rohan's Diet
        elif n2 == 2:
            t1 = getTime()                  # Calling the getTime() for Date & Time
            with open("Rohan_Diet", 'r') as f:  # opening Rohan's Diet in read mode
                print(t1, f.read())

        # Hamad's Diet
        elif n2 == 3:
            t1 = getTime()                  # Calling the getTime() for Date & Time
            with open("Hamad_Diet", 'r') as f:  # opening Hamad's Diet in read mode
                print(f.read())

    # for changing the Diet

    elif n1 == 2:
        n2 = int(input("Pres-s 1 for Harry's Diet, Press 2 for Rohan's Diet, Press 3 for Hamad's Diet:\n"))

        # Harry's Diet Chart(Write Mode)
        if n2 == 1:                         # Harry's Diet
            t1 = getTime()                  # Calling the getTime() for Date & Time
            data = input("Type Here :\n")
            with open("Harry_Diet", 'w') as f:  # opening Harry's Diet in 'write' mode
                f.write(str([str(getTime())]) + ": " + data + "\n")     # Converting the Date & Time into String and override the data
                # f.write(" " + data)
                print("!!!  Successful Entry    !!!")
            n3 = int(input("Press 1 if you want to change again Harry's Diet Chart or Press 2 for Previous Menu:\n"))
            if n3 == 1:             # for again changing the data in Harry's Diet
                with open("Harry_Diet", 'w') as f:       # opening Harry's Diet in write mode
                    print("Enter the Data you want to add.")
                    f.write(input(""))                  # overriding the data
                    print("!!!  Successful Entry    !!!")
            # elif n3 == 0 or n3 < 0 or n3 > 2:
            #     print("Wrong I/p. Try Again.")

        # Rohan's Diet Chart(Write Mode)
        elif n2 == 2:
            t1 = getTime()                  # Calling the getTime() for Date & Time
            data = input("Type Here :\n")
            with open("Rohan_Diet", 'w') as f:  # Rohan's Diet
                f.write(str([str(getTime())]) + ": " + data + "\n")      # Converting the Date & Time into String and override the data
                # f.write(" " + data)
                print("!!!  Successful Entry    !!!")
            n3 = int(input("Press 1 for changing Rohan's Diet Chart or Press Any Number for Previous Menu:\n"))
            if n3 == 1:         # for again changing the data in Rohan's Diet
                with open("Rohan_Diet", 'w') as f:    # opening Rohan's Diet in write mode
                    print("Enter the Data you want to add.")
                    f.write(input(""))              # overriding the data

        # Hamad's Diet Chart(Write Mode)
        elif n2 == 3:
            t1 = getTime()                  # Calling the getTime() for Date & Time
            data = input("Type Here :\n")
            with open("Hamad_Diet", 'w') as f:  # Hamad's Diet
                f.write(str([str(getTime())]) + ": " + data + "\n")     # Converting the Date & Time into String and override the data
                # f.write(" " + data)
                print("!!!  Successful Entry    !!!")
            n3 = int(input("Press 1 for changing Hamad's Diet Chart or Press Any Number for Previous Menu:\n"))
            if n3 == 1:         # for again changing the data in Hamad's Diet
                with open("Hamad_Diet", 'w') as f:         # opening Hamad's Diet in write mode
                    print("Enter the Data you want to add.")
                    f.write(input(""))           # overriding the data



def training(n):

    ''' This function makes files for creating Workout Plan of 3 people on everyday basis'''

    # with open("Harry_workout", 'w') as ha:  # Harry's Workout Plan
    #     ha.write("!! Harry's Workout Plan !!\nEvening:\n1 Push up\n2 Bench Press\n3 Dumbbell Press\n4 Cable Cross\n5 Dips\n\n")
    #
    # with open("Rohan_workout", 'w') as r:  # Rohan's Workout Plan
    #     r.write("!! Rohan's Workout Plan !!\nMorning:\n1 Diamond Push-up\n2 Lying Triceps\n3 Overhead Extension\n4 Triceps press Down\n\n")
    #
    # with open("Hamad_workout", 'w') as r:  # Hamad's Workout Plan
    #     r.write("!! Hamad's Workout Plan !!\nEvening:\n1 Pull Ups\n2 Lat Pull Down\n3 T-Bar\n4 Hyper-extension\n\n")

    t1 = getTime()  # for fetching time and date from system

    n1 = int(input("\nPress 1 to See the Workout Plan or Press 2 to Change the Workout Plan:\n"))

    # Read Only Mode for Workout Plan

    if n1 == 1:
        n2 = int(input("Press 1 for Harry's Workout Plan, Press 2 for Rohan's Workout Plan, Press 3 for Hamad's Workout Plan:"))

        # Harry's Workout Plan
        if n2 == 1:
            t1 = getTime()  # Calling the getTime() for Date & Time
            with open("Harry_workout", 'r') as f:  # opening Harry's Workout Plan in read mode
                print(t1, "\n", f.read())  # printing Harry's Workout Plan

        # Rohan's Workout Plan
        elif n2 == 2:
            t1 = getTime()  # Calling the getTime() for Date & Time
            with open("Rohan_workout", 'r') as f:  # opening Rohan's Workout Plan in read mode
                print(t1, f.read())             # printing Rohan's Workout Plan

        # Hamad's Workout Plan
        elif n2 == 3:
            t1 = getTime()  # Calling the getTime() for Date & Time
            with open("Hamad_workout", 'r') as f:  # opening Hamad's Workout Plan in read mode
                print(f.read())                 # printing Hamad's Workout Plan


    # for Changing the Workout Plan

    elif n1 == 2:
        n2 = int(input("Press 1 for Harry's Workout Plan, Press 2 for Rohan's Workout Plan, Press 3 for Hamad's Workout Plan:\n"))

        # Harry's Workout Plan(Write Mode)
        if n2 == 1:  # Harry's Workout Plan
            t1 = getTime()  # Calling the getTime() for Date & Time
            data = input("Type Here :\n")
            with open("Harry_workout", 'w') as f:  # opening Harry's Workout Plan in 'write' mode
                f.write(str([str(getTime())]) + ": " + data + "\n")  # Converting the Date & Time into String and override the data
                # f.write(" " + data)
                print("!!!  Successful Entry    !!!")
            n3 = int(input("Press 1 if you want to change again Harry's Diet Chart or Press 2 for Previous Menu:\n"))
            if n3 == 1:  # for again changing the data in Harry's Workout Plan
                with open("Harry_workout", 'w') as f:  # opening Harry's Workout Plan in write mode
                    print("Enter the Data you want to add.")
                    f.write(input(""))  # overriding the data
                    print("!!!  Successful Entry    !!!")
            # elif n3 == 0 or n3 < 0 or n3 > 2:
            #     print("Wrong I/p. Try Again.")

        # Rohan's Workout Plan Chart(Write Mode)
        elif n2 == 2:
            t1 = getTime()  # Calling the getTime() for Date & Time
            data = input("Type Here :\n")
            with open("Rohan_workout", 'w') as f:  # Rohan's Workout Plan
                f.write(str([str(getTime())]) + ": " + data + "\n")  # Converting the Date & Time into String and override the data
                # f.write(" " + data)
                print("!!!  Successful Entry    !!!")
            n3 = int(input("Press 1 for changing Rohan's Workout Plan or Press 2 for Previous Menu:\n"))
            if n3 == 1:  # for again changing the data in Rohan's Workout Plan
                with open("Rohan_workout", 'w') as f:  # opening Rohan's Workout Plan in write mode
                    print("Enter the Data you want to add.")
                    f.write(input(""))  # overriding the data

        # Hamad's Workout Plan(Write Mode)
        elif n2 == 3:
            t1 = getTime()  # Calling the getTime() for Date & Time
            data = input("Type Here :\n")
            with open("Hamad_workoutt", 'w') as f:  # Hamad's Workout Plan
                f.write(str([str(getTime())]) + ": " + data + "\n")  # Converting the Date & Time into String and override the data
                # f.write(" " + data)
                print("!!!  Successful Entry    !!!")
            n3 = int(input("Press 1 for changing Hamad's Workout Plan or Press 2 for Previous Menu:\n"))
            if n3 == 1:  # for again changing the data in Hamad's Workout Plan
                with open("Hamad_workout", 'w') as f:  # opening Hamad's Workout Plan in write mode
                    print("Enter the Data you want to add.")
                    f.write(input(""))  # overriding the data



a = 1
while a:            # Infinite Loop for continuous calling
    n = int(input("Press 1 for Diet Chart or Press 2 for Training Plan or Press 3 for Exit:"))
    if n == 1:
        diet(n)         # calling diet()
    elif n == 2:
        training(n)     # calling training()
    elif n == 3:
        sys.exit("Thank You")
    else:
        print("Wrong I/p. Try Again:")
        continue
