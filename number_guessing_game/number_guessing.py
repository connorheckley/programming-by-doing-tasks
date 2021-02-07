import random

random_number = random.randint(1,10)

print(random_number)
random_number = str(random_number)
tries = 0 

print("I have chosen a number between 1 and 10, try to guess it!")
guess = input("What number have you chosen: ")
tries +=1
while guess != random_number:
    guess = input("What number have you chosen: ")
    print("This is incorrect, you suck, guess again")
    tries +=1
if guess == random_number:
    print("Well done, your guess is correct!")
   
    print("Hit!\nIt took you " + str(tries) + " tries!")