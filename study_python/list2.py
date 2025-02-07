# 列表 list 2
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyota']
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']
print("=======================")
print(sorted(cars, reverse=True))  # ['toyota', 'subaru', 'bmw', 'audi']
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

cars2 = [2, 5, 3]
print(cars2)  # [2, 5, 3]
cars2.reverse()
print(cars2)  # [3, 5, 2]
cars2.reverse()
print(cars2)  # [2, 5, 3]
print(len(cars2))  # 3

# print(cars2[3]) # IndexError: list index out of range
cars3 = []
# print(cars3[-1]) # IndexError: list index out of range
