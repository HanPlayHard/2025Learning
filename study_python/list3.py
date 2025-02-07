# 列表 list 3
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
"""
alice
david
carolina
"""

for value in range(1, 5):
    print(value)
"""
1
2
3
4
"""

# print(range(1, 6))  # range(1, 6)
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]

even_numbers = list(range(2,11,2))
print(even_numbers) # [2, 4, 6, 8, 10]

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    # squares.append(value ** 2)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

digits = [1,2,3,4,5,6,7,8,9,10,999]
print(min(digits))#1
print(max(digits))#999
print(sum(digits))#1054

squares2 = [value**2 for value in range(1,11)]
print(squares2) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sum = 0
for value in range(1,1000001):
    sum+=value
print(sum) #500000500000