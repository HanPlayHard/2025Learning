# 列表 list 4, tuple

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])  # ['charles', 'martina', 'michael']
# print(players[:3])
print(players[1:])  # ['martina', 'michael', 'florence', 'eli']
print(players[-3:])  # ['michael', 'florence', 'eli']


for player in players[:3]:
    print(player.title())
# Charles
# Martina
# Michael

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print(my_foods)  # ['pizza', 'falafel', 'carrot cake']
print(friend_foods)  # ['pizza', 'falafel', 'carrot cake']

# 元组 Tuple
dimensions = (200, 50)
print(dimensions[0])  # 200
print(dimensions[1])  # 50
# dimensions[0]=250
# TypeError: 'tuple' object does not support item assignment

for dimension in dimensions:
    print(dimension)
"""
200
50"""
print(dimensions)  # (200, 50)
"""
Although you can't modify the elements of a tuple, you can assign
values to the variables that hold the tuple. Therefore, if you want to
Changing the dimensions of the preceding rectangle redefines the entire
 tuple:
虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要
修改前述矩形的尺寸，可重新定义整个元组：
"""
dimensions = (400, 100)
print(dimensions)  # (400, 100)

