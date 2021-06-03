''' Write a  programme which  will remind me after a specific time about 1. Drinking water 2. Washing Eyes
3. Doing some assignments . There must be some stopper word for each to stop that reminder. While the reminder is going on
an mp3 music should play in the background . Also there must be a file for each to show the timings of the reminders.
e.g. 1. drinking water - water.mp3 - (4 lits/day) - 'Drank'(stopper word) - water_log
'''
         # 1st

from pygame import mixer        # we can play music using pygame module
from datetime import datetime   # for date time
from time import time           # for time

def musicinloop(file, stopper):
    ''' This function takes the music file and a stopper word '''

    mixer.init()                # fetching the instances from mixer class
    mixer.music.load(file)      # load the music file
    mixer.music.play(-1)        # play that file for unlimited times
    while True:                 # infinite loop
        a = input()             # taking the stopper word
        if a == stopper:
            mixer.music.stop()  # stopping the music
            break

def log_water(msg):
    '''This function creates water-log file and stores all the timings  '''

    with open("water_log.txt", 'a') as f:       # opening the file in append mode
        f.write(f"{msg} {datetime.now()}\n")

def log_eye(msg):
    '''This function creates Eye-log file and stores all the timings  '''

    with open("eye_log.txt", 'a') as f:         # opening the file in append mode.
        f.write(f"{msg} {datetime.now()}\n")

def log_activity(msg):
    '''This function creates Activity-log file and stores all the timings  '''

    with open("activity_log.txt", 'a') as f:    # opening the file in append mode.
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == "__main__":

    # 3 variables for to store the timings
    init_water = time()
    init_eye = time()
    init_activity = time()

    # settings up the timings of the reminder
    watertime = 30 * 60
    eyetime = 60 * 60
    activitytime = 120 * 60

    while True:
        if time() - init_water > watertime:
            print("!!! Water Drinking Time !!! Enter 'drunk' to stop:\n")
            musicinloop("water.mp3", 'drunk')   # calling the music function
            init_water = time()             # resetting the time
            log_water("Drank Water at:")    #  calling the water_log function

        elif time() - init_eye > eyetime:
            print("!!! Eye Washing Time !!! Enter 'washed' to stop:\n")
            musicinloop("eye.mp3", 'washed')    # calling the music function
            init_eye = time()               # resetting the time
            log_eye("Washed Eye at:")       #  calling the Eye_log function

        elif time() - init_activity > activitytime:
            print("!!! Activity Time !!! Enter 'done' to stop:\n")
            musicinloop("activity.mp3", 'done')     # calling the music function
            init_activity = time()          # resetting the time
            log_activity("Done Activity at:")   #  calling the Activity_log function




        # 2nd
#
# from pygame import*
# from pygame import mixer
# import datetime
# import time
#
#
# def gettime():
# 	return (datetime.datetime.now())
#
#
# def watr():
#     time.sleep(1800)
#     file = 'water.mp3'
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play(10000, 0.0)
#     water = input('Please write "drank" to stop the reminder ')
#     if water == 'Drank' or 'drank':
#         mixer.music.pause()
#
#
# def eydone():
#     time.sleep(1800)
#     time.sleep(600)
#     file = 'eyes.mp3'
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play(10000, 0.0)
#     eyes = input('Please write "eydone" to stop the reminder ')
#     if eyes == 'Eydone' or eyes == 'eydone':
#         mixer.music.pause()
#         with open('eyes.txt', 'a') as f:
#             f.write(f'{gettime()} Eyes Exersice\n')
#
#
# def physical():
#     time.sleep(1800)
#     time.sleep(300)
#     file = 'physical.mp3'
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play(10000, 0.0)
#     exercise = input('Please write "exdone" to stop the reminder ')
#     if exercise == 'Exdone' or exercise == 'exdone':
#         mixer.music.pause()
#         with open('Exercise.txt', 'a') as f:
#             f.write(f'{gettime()} Physical Exersice\n')
#
#
# water_level = 0
# while water_level != 3500:
#     watr()
#     level = int(input('How much water did you drink '))
#     with open('water.txt','a') as f:
#         f.write(f'{gettime()} Water {level} ml\n')
#     water_level += level
#     print(f'{3500-water_level} ml remainig')
#     eydone()
#     physical()