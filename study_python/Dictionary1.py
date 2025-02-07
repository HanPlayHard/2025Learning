# Dictionary 字典


alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])  # green
print(alien_0["points"])  # 5

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
alien_0["color"] = "yellow"
print(alien_0["color"])  # yellow

my_test1 = {}
my_test1["points"] = 5
my_test1["1"] = "一"
print(my_test1)  # {'points': 5, '1': '一'}
del my_test1["points"]
print(my_test1)  # {'1': '一'}

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value + "\n")
"""
Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi"""

for k in user_0:
    print(k)
for k in user_0.keys():
    print(k)
"""
username
first
last
"""
print(user_0.keys())  # dict_keys(['username', 'first', 'last'])
print(sorted(user_0.keys()))  # ['first', 'last', 'username']
print(user_0.values())  # dict_values(['efermi', 'enrico', 'fermi'])
print("==============================")
user_0["add_test"] = "fermi"
print(user_0)
# {'username': 'efermi', 'first': 'enrico', 'last': 'fermi', 'add_test': 'fermi'}
print(set(user_0.values())) # {'enrico', 'fermi', 'efermi'}