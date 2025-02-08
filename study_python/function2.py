# 函数 fuction2
"""将函数存储在模块中:
假设我有个cool_boy.py模块,其中有函数function_test1,function_test2
Store functions in modules:
Let's say I have a cool_boy.py module with functions
function_test1,function_test2
"""

# 导入整个模块:Importing an entire module:
# import cool_boy
# cool_boy.function_test1(p1, p2)

# 导入特定的函数:Importing specific functions:
# from cool_boy import function_test1
# from cool_boy import function_test1, function_test2, function_test3

# 使用as 给函数指定别名:Use as to give a function an alias:
# from cool_boy import function_test1 as ft1

# 使用as 给模块指定别名:Use as to give the module an alias:
# import cool_boy as cb

# 导入模块中的所有函数:Import all the functions in the module
# from cool_boy import *

# ===================================
"""
建议代码行的长度不要超过79字符，这样只要编辑器窗口适中，就能看到整行代码。
We recommend that lines of code be no longer than 79 characters, 
so that entire lines of code can be viewed in a modest editor window.
"""

# ===================================
"""
如果形参很多，导致函数定义的长度超过了79字符:
If there are too many parameters to define a function
that is longer than 79 characters:
"""
# def function_test1(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     function body...

# ===================================
"""
编写函数时，应给函数指定描述性名称，且只在其中使用小写字母和下划线。
描述性名称可帮助你和别人明白代码想要做什么，给模块命名时也是这样
When you write functions, give them descriptive names and
use lowercase letters and underscores only. 
Descriptive names help you and others understand what your code is trying to do,
and the same goes for naming modules
"""

# ===================================
"""
每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后
面，并采用文档字符串格式。
Each function should include a comment that briefly explains what it does, 
immediately after the function definition, and in docstring format.
"""

# ===================================
"""
给形参指定默认值时|对于函数调用中的关键字实参，等号两边不要有空格：
When specifying default values for parameters | 
For keyword arguments in function calls, 
do not have Spaces around the equal sign:
def function_test1(parameter_0, parameter_1='default value')
function_test1(value_0, parameter_1='value')
"""

# ===================================
"""
所有的import语句都应放在文件开头，除非在文件开头使用了注释。
All import statements should be placed at the beginning of a file, 
unless you use comments at the beginning of the file.
"""