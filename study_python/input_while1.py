# while True:
#     print("true")
"""
true
true
true
true
...............
"""

message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# Tell me something, and I will repeat it back to you: Hello? Hello!
# Hello? Hello!

age = input("How old are you? ")  # How old are you? 24
print(age)  # 24
# print(age > 18)TypeError: '>' not supported between instances of 'str' and 'int'
age = int(age)
print(age > 19) # True

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
# Enter a number, and I'll tell you if it's even or odd: 24
if number % 2==0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")
# The number 24 is even.

current_number = 1
while current_number <=5:
    print(current_number)
    current_number+=1
"""
1
2
3
4
5
"""
# ==========================================================
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# ==========================================================
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

"""
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. 1111
1111

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) 2222
I'd love to go to 2222!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
"""

current_number = -1
while current_number <=10:
    current_number +=1
    if current_number %2==1:
        continue
    print(current_number)
"""
0
2
4
6
8
10
"""









