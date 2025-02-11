# 更新 pip : Update pip :
# python -m pip install --upgrade pip

# Install pytest:
# python -m pip install --user pytest


def get_formatted_name(first, last):
    """生成格式规范的姓名Generate name of format specification"""
    full_name = f"{first} {last}"
    return full_name.title()


def get_formatted_name2(first, middle, last):
    """生成格式规范的姓名Generate name of format specification"""
    full_name = f"{first} {middle} {last}"
    return full_name.title()


# The improved function get_formatted_name2
def get_formatted_name2_improved(first, last, middle=""):
    """生成格式规范的姓名Generate name of format specification"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


class AnonymousSurvey:
    """收集匿名调查问卷的答案
    The answers to the anonymous questionnaire were collected"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备
        Store a question and prepare for storing the answer"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷Display the survey questionnaire"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷
        Store single copies of survey responses"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷
        Display all the answers collected"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
