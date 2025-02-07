cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
"""
Audi
BMW
Subaru
Toyota
"""

print("Audi".lower() == "audi")  # True
print("Audi".lower() != "audi")  # False

age = 20
print(age < 20)  # False
print(age <= 20)  # True
age2 = 18
print(age >= 18 and age2 >= 18)  # True
print("===============================")
print(age >= 999 or age2 <= 20)  # True

requested_toppings = ["mushrooms", "onions", "pineapple"]
if "mushrooms" in requested_toppings:
    print("_nice boy_")
else:
    print("_oh man_")
# _nice boy_

requested_toppings2 = ["mushrooms", "onions", "pineapple"]
if "yyy" not in requested_toppings:
    print("_yes not_")
else:
    (print("_no in_"))
# _yes not_

if age >= 18:
    print("You can go work!")
# You can go work!

if age < 4:
    print("Your admission cost is free")
elif age < 18:
    print("Your admission cost is $0.09")
else:
    print("Your admission cost is $10000")
# Your admission cost is $10000

requested_toppings3 = []
if requested_toppings3:
    for requested_topping in requested_toppings3:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# Are you sure you want a plain pizza?

for num in range(1, 10):
    if num < 2:
        print(str(num) + "st")
    elif num < 3:
        print(str(num) + "nd")
    elif num < 4:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")
"""
1st
2nd
3rd
4th
5th
6th
7th
8th
9th"""

# My idea: Make a card game where two decks of three cards are compared in size,
# similar to Texas Hold 'em poker