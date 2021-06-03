# Create a dictionary & take i/p from the user & return the meaning of the word from the dictionary .


n = input("Enter the Name:")

d = {"Java": "Programming Language", "Facebook": "Social Media", "Google": "Website", "Yahoo": "Email"}

    # 1st type

# for k, v in d.items():
#     if k == n:
#         print(d[n])
#         exit()
#     else:
#         print("Wrong i/p ")
#         exit()

    #2nd type

n1 = n.capitalize()             # irrespective of the i/p's case it will show the o/p . Changing the case accordingly
print(n1, " = ", d[n1])


