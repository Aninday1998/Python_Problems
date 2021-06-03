''' Create a function called soldier . Which will take path of the folder, file name and format of the file as i/p.
it will change the file's 1st letter to capital letter those are txt file. Those files which are in 'jpg' format their
name will be converted into sequence of 1 to 10. '''


import os


def soldier(path, file, format):

    os.chdir(path)          # change the directory to the target folder
    i = 1
    files = os.listdir(path)        # storing the files names in a list
    with open(file) as f:           # opening the file
        filelist = f.read().split('\n')     # splitting when new line found

    for file in files:              # checking the file is present in that list or not
        if file not in filelist:
            os.rename(file, file.capitalize())      # if present switching it into capital letters

        if os.path.splitext(file)[1] == format:      # The 1st part([1]) returns the extension of the file.
            os.rename(file, f"{i} {format}")         # Which are in 'jpg' rename them from 1 to 10
            i += 1

soldier(r"C:\Users\Anindya Chatterjee\Desktop\Testing", r"E:/Python/Python Problems/ani.txt", ".jpg")