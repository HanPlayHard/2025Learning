from pathlib import Path
import json
import plotly.express as px
import pandas as pd

# 将数据作为字符串读取并转为Python对象
path = Path("eq_data/eq_data_30_day_m1.geojson")
try:
    contents = path.read_text()
except: # Windows 系统（默认编码是 GBK）
    contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)  # 这个文件的字符串表示转换为 Python 对象

# 将数据文件转换为更易于阅读的版本
path = Path("eq_data/eq_data_30_day_m1.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)  # 指定 元素的缩进量
path.write_text(readable_contents)


# 查看数据集中的所有地震
all_eq_dicts = all_eq_data["features"]  # 160
print(len(all_eq_dicts))

# 地震震级、位置（经度和纬度）等
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    title = eq_dict["properties"]["title"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])  # [1.6, 1.6, 2.2, 3.7, 2.92000008, 1.4, 4.6, 4.5, 1.9, 1.8]
print(titles[:2])  # ['M 1.6 - 27 km NNW of Susitna, Alaska', 'M 1.6 - 63 km SE
print(lons[:5])  # [-150.7585, -153.4716, -148.7531, -159.6267, -155.24833679
print(lats[:5])  # [61.7591, 59.3152, 63.1633, 54.5612, 18.7551670074463]
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=["经度", "纬度", "位置", "震级"]
)
data.head()

print(px.colors.named_colorscales())
"""
Plotly Express 有大量的渐变可供选择:
['aggrnyl', 'agsunset', 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 
'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'darkmint', 'electric', 
'emrld', 'gnbu', 'greens', 'greys', 'hot', 'inferno', 'jet', 'magenta', 'magma',
 'mint', 'orrd', 'oranges', 'oryel', 'peach', 'pinkyl', 'plasma', 'plotly3', 
 'pubu', 'pubugn', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 
 'rdpu', 'redor', 'reds', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'turbo', 
 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd', 'algae', 'amp', 'deep', 
 'dense', 'gray', 'haline', 'ice', 'matter', 'solar', 'speed', 'tempo', 
 'thermal', 'turbid', 'armyrose', 'brbg', 'earth', 'fall', 'geyser', 'prgn', 
 'piyg', 'picnic', 'portland', 'puor', 'rdgy', 'rdylbu', 'rdylgn', 'spectral', 
 'tealrose', 'temps', 'tropic', 'balance', 'curl', 'delta', 'oxy', 'edge', 
 'hsv', 'icefire', 'phase', 'twilight', 'mrybm', 'mygbm']
"""
# 地震散点图
fig = px.scatter(
    data,
    x="经度",
    y="纬度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
    # 定制标记的尺寸,
    size="震级",
    size_max=10,
    # size 参数来指定散点图中每个标记的尺寸
    color="震级", #从蓝色到红色再到黄色，数值越小标记越蓝，而数值越大则标记越黄
    hover_name='位置'
)
# fig.write_html("global_earthquakes.html")
fig.show()


