# >>> import this
# The Zen of Python, by Tim Peters 《Python之禅》，Tim Peters著
#
# Beautiful is better than ugly.#美丽总比丑陋好。
# Explicit is better than implicit.#显式比隐式好。
# Simple is better than complex.#简单胜于复杂。
# Complex is better than complicated.#复杂总比复杂好。
"""(现实是复杂的，有时候可能没有简单的解决方案。在这种情况下，就选择
最简单可行的解决方案吧。"""
# Flat is better than nested.#扁平化比嵌套更好。
# Sparse is better than dense.#稀疏比稠密好。
# Readability counts.#可读性很重要。
"""即便是复杂的代码，也要让它易于理解。开发的项目涉及复杂代码时，一
定要为这些代码编写有益的注释。"""
# Special cases aren't special enough to break the rules.#特殊情况没有特殊到可以打破规则。
# Although practicality beats purity.#尽管实用性胜过纯粹性。
# Errors should never pass silently.#错误不应该静默传递。
# Unless explicitly silenced.#除非明确静音。
# In the face of ambiguity, refuse the temptation to guess.#面对模棱两可的情况，拒绝猜测。
# There should be one-- and preferably only one --obvious way to do it.#应该有一种——最好只有一种——明显的方法来做到这一点。
"""大部分编程
工作都是使用常见解决方案来解决简单的小问题"""
# Although that way may not be obvious at first unless you're Dutch.#尽管这种方式一开始可能并不明显，除非你是荷兰人。
# Now is better than never.#现在总比没有好。
"""不要企图编写完美无缺的代码；先编写行之有效的代码，再
决定是对其做进一步改进，还是转而去编写新代码。"""
# Although never is often better than *right* now.#尽管“从不”通常比“现在”要好。
# If the implementation is hard to explain, it's a bad idea.#如果实现很难解释，那就不是一个好主意。
# If the implementation is easy to explain, it may be a good idea.#如果实现很容易解释，那么它可能是一个好主意。
# Namespaces are one honking great idea -- let's do more of those!#命名空间是一个非常棒的主意——让我们做更多的命名空间！

# fmt:on
# Ctrl + Alt + L      Format
user_name = "Hello man, would you like to learn some Python today?"
print(user_name)

name1 = " han play hard "
print(name1.lower())  # han play hard
print(name1.upper())  # HAN PLAY HARD
print(name1.title())  # HAN PLAY HARD

name2 = " John Johnson "
quote = "Great works not by strength, but by insist to complete."
message = "\t" + name2.strip() + " once said, \n" + '"' + quote + '"'
print(message)
"""		John Johnson once said, 
"Great works not by strength, but by insist to complete." """
print(0.2 + 0.1)  # 0.30000000000000004

print(name1.lstrip() + str(25) + " study")  # han play hard 25 study

print(3 / 2)  # 1.5(python3)       python2: 1
print(3.0 / 2)  # 1.5
print(3 / 2.0)  # 1.5
print(3.0 / 2.0)  # 1.5
print(4 * 2)  # 8
print(32 / 4)  # 8.0

# 基础补充，虽然好像没什么用
# Basic supplement, although it doesn't seem to be useful
print(name1.rstrip())
#  han play hard
print(name1.lstrip())
# han play hard
print(name1.strip())
# han play hard
print(name1.removeprefix(" han"))
#  play hard
print(name1.removesuffix("play hard "))
#  han
