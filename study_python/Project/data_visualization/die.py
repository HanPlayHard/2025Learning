from random import randint
import plotly.express as px


class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个介于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)


# 创建两个D6,(D6、D10)
die_1 = Die()
# die_2 = Die()
die_2 = Die(10)


# 投掷几次骰子，将结果存储在一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)
"""
[5, 6, 6, 3, 6, 3, 6, 1, 6, 5, 3, 3, 1, 1, 2, 1, 3, 4, 3, 5, 5, 3, 2, 3, 1, 1, 
5, 1, 5, 2, 3, 5, 4, 1, 1, 5, 5, 6, 1, 2, 6, 2, 2, 5, 6, 5, 2, 1, 2, 1, ......
"""

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
# poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)  # [152, 167, 183, 172, 172, 154]

# 对结果进行可视化
# title = "Results of Rolling One D6 1,000 Times"
# title = "Results of Rolling Two D6 Dice 1,000 Times"
title = "Results of Rolling a D6 and a D10  50,000 Times"

labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# 进一步定制图形
fig.update_layout(xaxis_dtick=1)  # 刻度标记的间距

# fig.write_html("dice_visual_d6_d10.html")  # 图形保存为 HTML 文件
"""
Plotly 将生成的直方图渲染为 HTML 文件，并在一个新的浏览器选项卡中显示
"""
fig.show()
