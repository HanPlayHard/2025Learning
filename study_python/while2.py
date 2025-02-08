monster_health = [999, 555, 444, 222, 123, 88, 77, 66, 55, 25, 45, 12, 9, 2, 1]
hero_health = 24
hero_exploits = 0
while monster_health:
    current_health = monster_health.pop()
    print("Current monster health: " + str(current_health))
    # Current monster health: 999
    if hero_health >= current_health:
        print("Hero wins")  # Hero wins
        hero_health += current_health
        hero_exploits += 1
    else:
        print("Hero die with honor")
        hero_health = -1
        break
print("\nThe hero_health: " + str(hero_health))
print("\nThe hero_exploits: " + str(hero_exploits))
# The hero_health: 2747
#
# The hero_exploits: 15

pets = [
    "cat0",
    "cat0",
    "dog",
    "cat0",
    "goldfish",
    "cat0",
    "cat",
    "rabbit",
    "cat0",
]
print(pets)
# ['cat0', 'cat0', 'dog', 'cat0', 'goldfish', 'cat0', 'cat', 'rabbit', 'cat0']
while 'cat0' in pets:
    pets.remove('cat0')
print(pets)
# ['dog', 'goldfish', 'cat', 'rabbit']

responses = {}
polling_active  =True
while polling_active:
    name = input("\n What is your name? ")
    response = input("Are you sure you love learning Python? (love or hate)")
    responses[name]=response
    repeat = input("End now or change the answer? (yes/no)")
    if repeat == 'yes':
        polling_active=False

print("\n---- Poll Results ---")
for name, response in responses.items():
    print(name+" "+response+" learn Python!")
"""
---- Poll Results ---
hanplayhard love learn Python!
hanplayhard1 love learn Python!
hanplayhard2 love learn Python!
hanplayhard3 love learn Python!
"""












