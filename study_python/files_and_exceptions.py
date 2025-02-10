from pathlib import Path
import json

path = Path("pi_digits.txt")
# path =Path('D:/Code/2025Learning/study_python/pi_digits.txt')

contents = path.read_text()
# contents = path.read_text().rstrip()
print(contents)
"""
3.1415926535
  8979323846
  2643383279
"""

lines = contents.splitlines()
pi_string = ""
for line in lines:
    # for line in contents.splitlines():
    pi_string += line

print(pi_string)  # 3.1415926535  8979323846  2643383279
print(len(pi_string))  # 36

pi_string = ""
for line in lines:
    pi_string += line.lstrip()
print(pi_string)  # 3.141592653589793238462643383279
print(pi_string[:4])  # 3.14
print(len(pi_string))  # 32

path2 = Path("programming.txt")
path2.write_text("I love programming.")

"""
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path3 = Path('programming3.txt')
path3.write_text(contents)
"""

try:
    print(5 / 0)
except ZeroDivisionError:
    # pass     # 让程序静默失败 Let the program fail silently
    print("You can't divide by zero!")  # You can't divide by zero!
else:
    print("answer")

path4 = Path("abcd.txt")
try:
    contents = path4.read_text(encoding="utf-8")
except FileNotFoundError:  # Sorry, the file abcd.txt does not exist.
    print(f"Sorry, the file {path4} does not exist.")

# 计算文件大致包含多少个单词
# Calculate roughly how many words the file contains
# words = contents.split()
# num_words = len(words)

# ==================================
numbers = [2, 3, 5, 6, 7, 9, 13]
path5 = Path("numbers.json")
contents = json.dumps(numbers)
path5.write_text(contents)  # [2, 3, 5, 6, 7, 9, 13]

contents2 = path5.read_text()
# if path5.exists():
numbers2 = json.loads(contents2)
print(numbers2)  # [2, 3, 5, 6, 7, 9, 13]
