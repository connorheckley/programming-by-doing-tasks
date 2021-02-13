pokeParty = ["Pikachu", "Charmeleon", "Geodude", "Gyrados", "Butterfree", "Mankey"]

print("Exchange Pokemon")
print("0. " + pokeParty[0])

for i in range(len(pokeParty)):
    print(f"\t  {i}   {pokeParty[i]}")

print(f"\nChoose a Pokemon to exchange with {pokeParty[0]} (Or enter 0 to quit.)")
x = int(input("> "))

if x == 0:
    quit()
elif x == 1:
    print("Charmeleon")
    pokeParty[1] = pokeParty[0]
    pokeParty[0] = 'Charmeleon'
elif x == 2:
    print("Geodude")
    pokeParty[2] = pokeParty[0]
    pokeParty[0] = 'Geodude'
elif x == 3:
    print("Gyrados")
    pokeParty[3] = pokeParty[0]
    pokeParty[0] = 'Gyrados'
elif x == 4:
    print("Butterfree")
    pokeParty[4] = pokeParty[0]
    pokeParty[0] = 'Butterfree'
elif x == 5:
    print("Mankey")
    pokeParty[5] = pokeParty[0]
    pokeParty[0] = 'Mankey'
else:
    print("Invalid Error")

for i in range(len(pokeParty)):
    print(f"\t  {i}   {pokeParty[i]}")