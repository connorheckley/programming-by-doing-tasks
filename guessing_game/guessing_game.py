import random

num = random.randint(1, 10)

# print(num)

num = str(num)

print("Guess the number between 1 and 10!")

guess = input("Your guess: ")
while guess != num:
    print("That is incorrect, guess again!")
    if guess  > num:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    guess = input("Your guess: ")
    if guess == num:
        print("You Got it!")