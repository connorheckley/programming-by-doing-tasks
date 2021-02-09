message = input("What is your message?: ")

length_of_message = len(message)

print("Your message is: ", length_of_message)
print("The first character is at 0 and it is:", message[0])
print("The last chartacter is at position {} and is {}.".format(length_of_message-1, message[-1]))
print()
print("Here are all the characters, one at a time:")
print()
letter = 0
for i in range(0,length_of_message):
    print(i, '-', message[i])
    if message[i] == 'a':
        letter += 1
    
print("Your message contains the letter 'a'", letter)