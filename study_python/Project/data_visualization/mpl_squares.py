import matplotlib.pyplot as plt

"""
subplots() 函数,可在一个图形（figure）中绘制一或多个绘图（plot）。
变量 fig 表示由生成的一系列绘图构成的整个图形。
变量 ax表示图形中的绘图，在大多数情况下，使用这个变量来定义和定制绘图。
plt.show() 函数打开 Matplotlib 查看器并显示绘图
"""
input_values=[1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置主题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

print(plt.style.available)
"""
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', 
'_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 
'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'seaborn-v0_8', 
'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 
'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 
'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 
'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 
'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 
'tableau-colorblind10']
"""
plt.show()
