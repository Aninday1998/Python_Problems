    #   Library Management System


                        #  1st Solution

import sys


class Library:

    def __init__(self, lib_name):
        self.list_books = {1: 'Feluda', 2: 'Sharlock Holmes', 3: 'Tenida', 4: 'Pandab Goyenda', 5: 'Sonar Kella'}
        self.lib_name = lib_name


    def display(self):

        print("Your Book-list is :\n ")
        for key, values in self.list_books.items():
            print(key, values)
            # print(f"{key} {values}")

    def lend(self):

        while True:
            n = int(input("\nPress 1 to Lend Book\nPress 2 to Back"))
            if n == 1:
                print("\nPls. Select the Index No.of the Book from these:\n")
                for key, values in self.list_books.items():
                    print(key, values)
                n1 = int(input())
                for key in self.list_books:
                    if key == n1:
                        break
                self.list_books.__delitem__(n1)
                # del self.list_books[n1]
                print("Successful lending .\n")

                # print("Available Book are")
                # for key, values in self.list_books.items():
                #     print(key, values)

            elif n == 2:
                break
            else:
                print("Wrong input. Pls. Try Again")
                continue

    def donate(self):
        while True:
            n = int(input("\nPress 1 to Donate Book\nPress 2 to Back"))
            if n == 1:
                n1 = int(input("Enter the index no. of the book:\n"))
                n2 = input("Enter the name of the book:\n")
                self.list_books.update({n1: n2})
                print("Thank You for Donation.")
                # print("Available Book are")
                # for key, values in self.list_books.items():
                #     print(key, values)

            elif n == 2:
                break
            else:
                print("Wrong input. Pls. Try Again.\n")
                continue


    def return_book(self):

        while True:
            n = int(input("Press 1 to return your book:\nPress 2 to Back:"))
            if n == 1:
                n1 = int(input("Enter the index no. of the book:\n"))
                n2 = input("Enter the name of the book:\n")
                self.list_books.update({n1: n2})
                print("Return Successful.")

                print("Available Book are")
                for key, values in self.list_books.items():
                    print(key, values)
            elif n == 2:
                break
            else:
                print("Wrong input. Pls. Try Again.\n")
                continue




def main():

    def begin(key_user):

        # print(key_user[i])
        x = key_user[i]

        key_user[i] = Library(f"{x}'s Library")

        print(f"\n!! Welcome to {x}'s Library !!")
        while True:
            n = int(input("\nPress 1 to Display Book-List\nPress 2 to Lend a book\nPress 3 to Donate a book\nPress 4 to Return a book\nPress 5 to Exit:\n"))
            if n == 1:
                key_user[i].display()
            elif n == 2:
                key_user[i].lend()
            elif n == 3:
                key_user[i].donate()
            elif n == 4:
                key_user[i].return_book()
            elif n == 5:
                sys.exit("Thank You")
            else:
                print("Wrong input. Pls. Try again")



    key_user = ["Harry", "Rohan", "Bitan"]

    x = int(input("Press 1 if You are an Existing User\nPress 2 if you want to create an New User\nPress 3 for exit:\n"))
    if x == 1:                                                   # Existing User
        u = input("Enter your name:")
        u = u.capitalize()
        for i in range(0, len(key_user)):
            if key_user[i] == u:
                # print(f"User Found {key_user[i]}")
                begin(key_user)
                break
        else:
            print("User Not found")

    elif x == 2:        # New User
        u = input("Enter your name:")
        u = u.capitalize()
        key_user.append(u)
        print("\nUser Created Successfully\n")
        for i in range(0, len(key_user)):
            if key_user[i] == u:
                # print(f"User Found {key_user[i]}")
                begin(key_user)
                break

    elif x == 3:
        sys.exit("Thank You")
    else:
        print("Wrong input. Try Again")







if __name__ == "__main__":
    main()




                        # 2nd Solution

#
#
# # Create a library class
# # display book
# # lend book - (who owns the book if not present)
# # add book
# # return book
#
# # HarryLibrary = Library(listofbooks, library_name)
#
#
# #dictionary (books-nameofperson)
#
# # create a main function and run an infinite while loop asking
# # users for their input
#
#
# class Library:
#     def __init__(self, list, name):
#         self.booksList = list
#         self.name = name
#         self.lendDict = {}
#
#     def displayBooks(self):
#         print(f"We have following books in our library: {self.name}")
#         for book in self.booksList:
#             print(book)
#
#     def lendBook(self, user, book):
#         if book not in self.lendDict.keys():
#             self.lendDict.update({book:user})
#             print("Lender-Book database has been updated. You can take the book now")
#         else:
#             print(f"Book is already being used by {self.lendDict[book]}")
#
#     def addBook(self, book):
#         self.booksList.append(book)
#         print("Book has been added to the book list")
#
#     def returnBook(self, book):
#         self.lendDict.pop(book)
#
# if __name__ == '__main__':
#     harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")
#
#     while(True):
#         print(f"Welcome to the {harry.name} library. Enter your choice to continue")
#         print("1. Display Books")
#         print("2. Lend a Book")
#         print("3. Add a Book")
#         print("4. Return a Book")
#         user_choice = input()
#         if user_choice not in ['1','2','3','4']:
#             print("Please enter a valid option")
#             continue
#
#         else:
#             user_choice = int(user_choice)
#
#
#         if user_choice == 1:
#             harry.displayBooks()
#
#         elif user_choice == 2:
#             book = input("Enter the name of the book you want to lend:")
#             user = input("Enter your name")
#             harry.lendBook(user, book)
#
#         elif user_choice == 3:
#             book = input("Enter the name of the book you want to add:")
#             harry.addBook(book)
#
#         elif user_choice == 4:
#             book = input("Enter the name of the book you want to return:")
#             harry.returnBook(book)
#
#         else:
#             print("Not a valid option")
#
#
#         print("Press q to quit and c to continue")
#         user_choice2 = ""
#         while(user_choice2!="c" and user_choice2!="q"):
#             user_choice2 = input()
#             if user_choice2 == "q":
#                 exit()
#
#             elif user_choice2 == "c":
#                 continue

