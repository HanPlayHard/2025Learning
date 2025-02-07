# Dictionary 字典2
# 嵌套 Nest
# ===========================================
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
"""
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
"""

aliens1 = []
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens1.append(new_alien)

for alien in aliens1[:5]:
    print(alien)
print("==============================")
print("Total number of aliens: " + str(len(aliens1)))
# Total number of aliens: 30
# ===========================================
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

print(pizza["crust"])  # thick
print(pizza["toppings"])  # ['mushrooms', 'extra cheese']
# ===========================================
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for user_name,user_info in users.items():
    print("\nUsername: "+user_name)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']

    print("\tFull_name: "+full_name.title())
    print("\tLocation: "+location.title())
"""

Username: aeinstein
	Full_name: Albert Einstein
	Location: Princeton

Username: mcurie
	Full_name: Marie Curie
	Location: Paris
"""

