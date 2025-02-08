# 一、基础语法快速掌握
# 1.	变量与数据类型
name = "HanPlayHard"  # 字符串
age = 25  # 整数
score0 = 99.99  # 浮点数
is_student = True  # 布尔值

# 2.	控制结构
# 	条件判断
score1 = 99
if score1 >= 90:
    print("A")  # A
elif score1 >= 60:
    print("Pass")
else:
    print("Fail")
# 循环结构
# for循环
for i in range(5):
    print(i)  # 输出0-4
    # break
    # continue
"""
0
1
2
3
4
"""

# while循环
count = 0
while count < 3:
    print(count)
    count += 1
"""
0
1
2
"""


# 3.	函数与模块
# 定义函数
def greet(name1, name2="", **name3):
    return "Hello " + name + "!"
    # return f"Hello, {name}!"
    # for key, value in name3.items():
    #     list_test[key] = value


# 调用函数  Hello HanPlayHard!
print(greet("hanplayhard", "22", name3="33", n4="44"))


def greet2(name1, name2="", *name3):
    return "Hello " + name3[0] + "!"
    # return f"Hello, {name}!"
    # for name in name3:
    #     print(name)


# Hello 33!
print(greet2("hanplayhard", "22", "33", "44", "55"))


# 导入模块
import math

print(math.sqrt(16))  # 4.0


# 二、核心数据结构
# 1.	列表（可变序列）;  用小括号定义变为： 不可修改的元组 tuple
fruits2 = ["apple", "banana", "cherry"]
fruits2.append("orange")  # 添加元素
print(fruits2[1:3])  # 切片输出 ['banana', 'cherry']

# 2.	字典（键值对集合）
user = {"name": "hanplayhard", "age": 24, "email": "hanplayhard@example.com"}
print(user["name"])  # hanplayhard
print(user.get("age", 0))  # 安全获取值  24
