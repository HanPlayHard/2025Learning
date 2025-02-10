"""
当你让 pytest 运行测试时，它将查找以 test_打头的文件，并运行其中的所有测试。
When you tell pytest to run tests, it looks for the file that starts with test_
 and runs all the tests in that file.
"""

from code_test_pytest import *


# test_xxxxxxxx
def test_first_last_name():
    """能够正确地处理像 Hanplay Hard 这样的姓名吗？
    Can you handle a name like Hanplay Hard correctly?"""
    formatted_name = get_formatted_name("hanplay", "hard")
    assert formatted_name == "Hanplay Hard"


# 打开一个终端窗口Open a terminal window:    $   pytest
"""
============================================= test session starts ==============
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: D:\study_python
collected 1 item                                                                                                

test_name_function.py .                                                   [100%] 

============================================== 1 passed in 0.01s ===============
"""

# # test_xxxxxxxx
# def test_first_last_name2():
#     """能够正确地处理像 Hanplay Hard 这样的姓名吗？
#     Can you handle a name like Hanplay Hard correctly?"""
#     formatted_name = get_formatted_name2("hanplay", "hard")
#     assert formatted_name == "Hanplay Hard"

# F: 表明有测试未通过: Indicates that a test has failed
# E:指出了导致测试未通过的具体错误:
# Indicates the specific error that caused the test to fail

"""
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: D:\study_python
collected 2 items                                                                                               

test_name_function.py .F                                                  [100%]

================================================== FAILURES ====================
____________________________________________ test_first_last_name2 _____________

    def test_first_last_name2():
        能够正确地处理像 Hanplay Hard 这样的姓名吗？
        Can you handle a name like Hanplay Hard correctly?
        
>       formatted_name = get_formatted_name2("hanplay", "hard")
E       TypeError:
 get_formatted_name2() missing 1 required positional argument: 'last'

test_name_function.py:33: TypeError
============================================== warnings summary ================
test_name_function.py:18
  D:\study_python\test_name_function.py:18: 
  SyntaxWarning: invalid escape sequence '\s'       


-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================================== short test summary info ============
FAILED test_name_function.py::test_first_last_name2 - TypeError: 
get_formatted_name2() missing 1 required positional argument: 'last'
=================================== 1 failed, 1 passed, 1 warning in 0.04s =====
"""


# test_xxxxxxxx
def test_first_last_name2_1():
    """能够正确地处理像 Hanplay Hard 这样的姓名吗？
    Can you handle a name like Hanplay Hard correctly?"""
    formatted_name = get_formatted_name2_improved("hanplay", "hard")
    assert formatted_name == "Hanplay Hard"
# ======================================== 2 passed, 2 warnings in 0.01s ===

def test_first_last_middle_name():
    """能够正确地处理像 Han Play Hard 这样的姓名吗？
    Can you handle a name like Han Play Hard correctly?"""
    formatted_name = get_formatted_name2_improved("han",
                                                  "Hard", "Play")
    assert formatted_name == "Han Play Hard"
# ======================================== 3 passed, 2 warnings in 0.01s ===