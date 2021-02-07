""" Library """

import os
import time


# login screen

# login validation

# logout
os.system('cls')


def login_screen():

    os.system('clear||cls')

    print("\t=================")
    print("\tNewcastle Library")
    print("\t=================\n")
    
    username = input("\tWhat is your username? ")
    password = input("\tWhat is your password? ")

    details = [username, password]
    login_validation(details)

def login_validation(details):
    username = details[0]
    password = details[1]

    try:
       f = open("database.txt", "r")
       logins = f.read()
       logins = logins.split('\n')

       if username in logins:
           os.system('clear||cls')
           name = input("\t\nProvide your name: ")
           age = input("\tProvide your age: ")
           address = input("\tProvide your address: ")

           user1 = User(name, username, password, age, address)

           os.system('clear||cls')

           print()
           print("\n\t1. Rent a book")
           print("\t2. Rent a CD")
           print("\t3. Return a book")
           print("\t4. Return a CD")

           option = input(">")

           if option == '1':
               book = Book(user_input(),user_input(),user_input() )

           elif option == '2':
               cd = CD()
               cd.title(user_input())
               cd.date(user_input())
               cd.author(user_input())
           elif option == '3':
               book = Book()
               book.title(user_input())
           elif option == '4':
               book = Book()
               book.title(user_input())
           else: 
                print("Input Error")
       else:
           f = open("database.txt", "a")
           f.write(username + "\n")
           f.write(password + "\n")
           f.close()

           print("\tDatabase updated. New user created!")
           print("\tPlease Login")
           time.sleep(2)
           login_screen()
           # app run

    except FileNotFoundError:
       pass 
       
def logout():
    question = input("Would you like to logout? (y,n): ")
    if question == 'y':
        pass
    else:
            # something else
        pass

def user_input():
    user_input = input()

class User:
    def __init__(self, username, password, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.username = username
        self.password = password

    def rent_item():
        pass

    def return_item():
        pass

class Book(object):
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

class CD:
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date


if __name__ == "__main__":
    login_screen()


