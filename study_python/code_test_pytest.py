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
