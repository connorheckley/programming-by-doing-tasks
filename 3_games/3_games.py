import random

username = 'Newcastle'
password = 12345

def intro():
    print("\n//////////////////////////////////////")
    print("\tGAMES")
    print("//////////////////////////////////////")

def login():
    print("Please enter your login details!\n ")
    u = input("Please enter your username! :")
    p = int(input("Please enter your password! :"))

    if u == username:
         if p == password:
             menu()
    else:
        game_exit()

def game1():
    
    name = get_name()

    random_number = random.randint(1,6)
    wishes = ['wish1', 'wish2','wish3', 'wish4','wish5', 'wish6']
    print(random_number)
    if random_number == 1:
        print(wishes[0], name)
    elif random_number == 2:
        print(wishes[1], name)
    elif random_number == 3:
        print(wishes[2], name)
    elif random_number == 4:
        print(wishes[3], name)
    elif random_number == 5:
        print(wishes[4], name)
    elif random_number == 6:
        print(wishes[5], name)
    else:
        print("Invalid Input")

def game2():

    name = get_name()

    print("Im thinking of a number between 1, 100. Try to guess it!")
    guess = 0
    random_number = random.randint(1,100)

    while guess != random_number:
        guess = int(input("> "))
        if guess > random_number:
            print("Youre guess is too high!")
        elif guess < random_number:
            print("Your guess is too low")
        else:
            print("You guessed it, well done!", name)

def game3():

    word = input("Provide the word!:")
    # radek
    word_list = []
    
    for i in word:
        word_list.append(i)

    length = len(word_list)

    for i in range(length-1, 0, -1):
        print(word_list[i], end=' ')


def menu():
    print("\nMenu\n")
    print("1. Wishes Game")
    print("2. Number Guessing Game")
    print("3. Credits")
    print("4. Quit")
    print("5. Reverse Word Game")

    choice = input("Which option do you want to choose?: ")
    if choice == '1':
        game1()
    elif choice == '2':
        game2()
    elif choice == '3':
        game_credits()
    elif choice == '4':
        game_exit()
    elif choice == '5':
        game3()
    else:
        print("Invalid Input")

def game_credits():
    print("\n//////////////////////////////////////////////////////")
    print("\nThis game was made by Radek Warowny and Connor Heckley")
    print("\n//////////////////////////////////////////////////////")
    n = input()
    menu()

def game_exit():
    quit()

def get_name():
    name = input("Please provide your name: ")
    return name
    

intro()
login()
