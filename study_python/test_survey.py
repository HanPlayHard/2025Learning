from code_test_pytest import AnonymousSurvey
import pytest


def test_store_single_response():
    """测试单个答案会被妥善地存储
    Test that a single answer is stored properly"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses


"""
collected 1 item

test_survey.py .                                                          [100%]

======================================== 1 passed in 0.02s =====================
"""


def test_store_single_response3():
    """测试三个答案会被妥善地存储
    The test three answers are stored properly"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ["English", "Spanish", "Mandarin"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses


"""
collected 2 item

test_survey.py ..                                                         [100%]

======================================== 1 passed in 0.02s =====================
"""

# 使用夹具
# 让使用该资源的每个测试函数都接受一个与该函数同名的形参
# Let each test function that uses the resource take a parameter
# with the same name as the function
"""
要创建夹具，可编写一个使用
装饰器 @pytest.fixture 装饰的函数。装饰器（decorator）是放在函
数定义前面的指令。在运行函数前，Python 将该指令应用于函数，以修
改函数代码的行为。
To create a fixture, write one that uses
Decorator @pytest.fixture decorates the function. Decorators are placed on 
functions
The number defines the preceding instruction. 
Python applies this instruction to the function to fix it before running it
Change the behavior of the function code.
"""


@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的 AnonymousSurvey 实例
    An instance of AnonymousSurvey that can be used by all test functions"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    """测试单个答案会被妥善地存储"""
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_three_responses(language_survey):
    """测试三个答案会被妥善地存储"""
    responses = ["English", "Spanish", "Mandarin"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses


"""
collected 3 item

test_survey.py ...                                                        [100%]

======================================== 1 passed in 0.02s =====================
"""
