# 函数 fuction1


def greet_user():
    """Display a simple greeting"""
    print("Hello!")


greet_user()  # Hello!


# =================================
def greet_user(username1, username2):
    """Display a simple greeting"""
    print("Hello, " + username1.title() + "!")
    print("Hi, " + username2.title() + ".")


# Positional arguments 位置实参
greet_user("hanplayhard", "boy")
"""
Hello, Hanplayhard!
Hi, Boy.
"""


# =================================
def greet_user2(username1, username2="default_username"):  # 默认值 Default values
    """Display a simple greeting"""
    print("Hello, " + username1.title() + "!")
    print("Hi, " + username2.title() + ".")


# 关键字实参 Keyword arguments
greet_user2(username2="222", username1="1111111")
"""
Hello, 1111111!
Hi, 222.
"""
greet_user2(username1="1111111")
"""
Hello, 1111111!
Hi, Default_Username.
"""


# =================================
def get_formatted_name(first_name, last_name):
    """Returns a clean name"""
    full_name = first_name + " " + last_name
    return full_name.title()


a_cool_man = get_formatted_name("han", "playhard")
print(a_cool_man)  # Han Playhard


# ================================= dictionary
def build_person(first_name, last_name, p3="cool", p4="inspirational"):
    """Returns a dictionary containing information about a person"""
    person = {"first": first_name, "last": last_name, "image": p3, "character": p4}
    return person


my1 = build_person("han", "playhard")
print(my1)
# {'first': 'han', 'last': 'playhard', 'image': 'cool',
# 'character': 'inspirational'}


# ================================= list
def greet_users(names):
    """Send a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ["hanplayhard", "man", "hahahaha", "love"]
greet_users(usernames)
"""
Hello, Hanplayhard!
Hello, Man!
Hello, Hahahaha!
Hello, Love!
"""


"""
将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做
的任何修改都是永久性的，这让你能够高效地处理大量的数据。
When you pass a list to a function, the function can modify it.
What you do to the list inside the function Any chawnges to is permanent,
which allows you to process large amounts of data efficiently.
"""


def greet_users2(names2):
    """Send a simple greeting to each user in the list"""
    for name in names2:
        if name == "love":
            names2[3] = "love2"
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames2 = ["hanplayhard", "man", "hahahaha", "love"]
greet_users2(usernames2)
print(usernames2)
"""
Hello, Hanplayhard!
Hello, Man!
Hello, Hahahaha!
Hello, Love!
['hanplayhard', 'man', 'hahahaha', 'love2']
"""

"""有时候，需要禁止函数修改列表,可以将列表的副本传递给函数
Sometimes I need to prevent a function from modifying a list, so I
can pass a copy of the list to the function
"""
# like this:
# greet_users2(usernames2[:])

# =================================传递任意数量的实参
# Pass an arbitrary number of arguments
# def greet_users(p1, p2, *names)


# =================================使用任意数量的关键字实参
# Use any number of keyword arguments
"""
形参**user_info 中的两个星号让
Python创建一个名为user_info 的空字典，并将收到的所有名称—值对
都封装到这个字典中。
The two asterisks in the parameter **user_info let
Python creates an empty dictionary called user_info and 
takes all the name-value pairs it receives
All wrapped up in this dictionary.
"""


def case1(p1, p2, **user_info):
    profile = {}
    profile["first_name"] = p1
    profile["last_name"] = p2
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = case1("aa", "bbb", p_c="cool", p_d="damn")
print(user_profile)
# {'first_name': 'aa', 'last_name': 'bbb', 'p_c': 'cool', 'p_d': 'damn'}
