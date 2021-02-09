''' Black Jack Game '''
''' Inspired by Programming by Doing '''

import random

print("Welcome to Mitchells Blackjack Program!")

card_one = random.randrange(2,11)
card_two = random.randrange(2,11)

player_total = card_one + card_two

print(f"You get a {card_one} and {card_two}")
print(f"Your total is {card_one+card_two}\n")

if player_total > 21:
    print("Bust. Your total is over 21. Game Over")
    quit()

dealers_card = random.randrange(2,11)
dealers_hidden_card = random.randrange(2,11)
print(f"The dealer has a {dealers_card} showing and a hidden card.")
print("His total is hidden too!\n")

question = input("Would you like to hit or stay?: ")

while question == 'hit':
    card = random.randrange(2,11)
    print(f"You drew a {card}")
    player_total += card
    print("Your total is: ", player_total)
    if player_total > 21:
        print("Bust. Your total is over 21. Game Over")
        quit()
        
    question = input("Would you like to hit or stay?")

print("Ok, dealer's turn.")
print("His hiddencard was a ", dealers_hidden_card)
print("His total is ", dealers_card+dealers_hidden_card)

dealers_total = dealers_card + dealers_hidden_card
dealers_choice = random.randrange(0,1)
if dealers_choice == 0:
    print("Dealer chooses to hit!")
    card = random.randrange(2,11)
    print(f"He draws a {card}")
    dealers_total += card
    print("His total is: ", dealers_total)
else:
    print("Dealers stays.")

if dealers_total >= 21:
    print("Bust. Your total is over 21. Game Over")
    quit()

print("Dealers total is:", dealers_total)
print("Your total is: ", player_total)

if dealers_total > player_total:
    print("Dealer wins")
else:
    print("Congratulations, you win!")