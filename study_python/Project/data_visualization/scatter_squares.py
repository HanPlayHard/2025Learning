import matplotlib.pyplot as plt

# 绘制点， scatter() ，传递 x,y 坐标值

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
# 参数 s 设置绘图时使用的点的尺寸,数据点的颜色，color=(0, 0.8, 0)
# ax.scatter(x_values, y_values, color="red", s=10)
# 颜色映射colormap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置主题，给坐标加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")  # 刻度标记Matplotlib 默认使用科学记数法
# 设置刻度标记的样式
ax.tick_params(labelsize=14)
plt.show()

# 将绘图保存到文件中
"""
第一个实参指定 文件名保存绘图，将被存储到scatter_squares.py 所在的目录中。
第二个实参指定将绘图多余的空白区域裁剪掉
"""
# plt.savefig('squares_plot.png', bbox_inches='tight')
