import random

""" Fortune Cookie """

__author__ = "Connor Heckley"
__status__ = "Education Program"

"""
    A beautiful, smart, and loving person will be coming into your life.
    A dubious friend may be an enemy in camouflage.
    A faithful friend is a strong defense.
    A feather in the hand is better than a bird in the air. ( ...
    A fresh start will put you on your way.
    A friend asks only for your time not your money.

"""

# print(random.randint(0,6))
random_number = random.randint(1,6) # random module generates random int

# list holds sayings
fortune_cookie_saying = ['A beautiful, smart, and loving person will be coming into your life.', 
'A dubious friend may be an enemy in camouflage.','A feather in the hand is better than a bird in the air.',
'A faithful friend is a strong defense.','A fresh start will put you on your way.','A friend asks only for your time not your money.']

print("Fortune Cookie: \n")

if random_number == 1:
    print(fortune_cookie_saying[0])
elif random_number == 2:
    print(fortune_cookie_saying[1])
elif random_number == 3:
    print(fortune_cookie_saying[2])
elif random_number == 4:
    print(fortune_cookie_saying[3])
elif random_number == 5:
    print(fortune_cookie_saying[4])
elif random_number == 6:
    print(fortune_cookie_saying[5])

else:
    print("You have no fortune")

print("Lotto Numbers: \n")
for i in range(1,6):
    random_lottonumber = random.randint(1,54)
    print(random_lottonumber , end=(' - '))