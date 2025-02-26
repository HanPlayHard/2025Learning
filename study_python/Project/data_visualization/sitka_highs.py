from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)  # 包含 CSV 文件中各行的列表
header_row = next(reader)  #  返回文件中的下一行（从文件开头开始）
# print(header_row)

for index, column_header in enumerate(header_row):  # 获取每个元素的索引及其值。
    print(index, column_header)


# # 提取最高温度
# highs = []
# """
# reader 对象从刚才中断的地方继续往下读取 CSV 文件，每次
# 都自动返回当前所处位置的下一行。由于已经读取了文件头行，这个循环
# 将从第二行开始——从这行开始才是实际数据
# """
# for row in reader:
#     high = int(row[4])
#     highs.append(high)
# print(highs)

# 日期
first_date = datetime.strptime("2025-02-25", "%Y-%m-%d")
print(first_date)  # 2025-02-25 00:00:00
"""
%A 星期几，如 Monday
%B 月份名，如 January
%m 用数表示的月份（01～12）
%d 用数表示的月份中的一天（01～31）
%Y 四位数的年份，如 2019
%y 两位数的年份，如 19
%H 24 小时制的小时数（00～23）
%I 12 小时制的小时数（01～12）
%p am 或 pm
%M 分钟数（00～59）
%S 秒数（00～61）
"""

# 提取日期和最高温度
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# # 根据最高温度绘图
# plt.style.use("fivethirtyeight")
# fig, ax = plt.subplots()
# ax.plot(highs, color="red")

# # 设置绘图的格式
# ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
# ax.set_xlabel("", fontsize=16)
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()


# 根据数据绘图
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5, linewidth=2)
ax.plot(dates, lows, color="blue", alpha=0.5, linewidth=1)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# 设置绘图的格式
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
