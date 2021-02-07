""" Pin LOCKOUT """ 
pin = 27786
pin = str(pin)
tries = 0

print("Welcome to the Bank of Gateshead!")
entry = input("Please enter your pin: ")
tries +=1

while (entry != pin and tries < 3):
    print("\nIncorrect pin, Please Try Again.")
    entry = input ("Please enter your pin: ")
    tries +=1
    
if (entry == pin):
    print("\nPin accepted, you now have access.")
else:
    (tries >= 3)
    print("\nYou have entered too many incorrect pins, account locked.")