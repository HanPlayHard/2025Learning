from PIL import Image

def convert_png_to_ico(png_path, ico_path, size=(64, 64)):
    """
    将PNG图片转换为ICO图标。
    
    :param png_path: 输入的PNG文件路径
    :param ico_path: 输出的ICO文件路径
    :param size: 图标大小，默认为(64, 64)
    """
    # 打开PNG图片
    image = Image.open(png_path)
    
    # 调整图片大小
    image = image.resize(size, Image.LANCZOS)
    
    # 保存为ICO格式
    image.save(ico_path, format='ICO')

# 示例用法
png_file = './Han.png'  # 替换为你的PNG文件路径
ico_file = './Han.ico'   # 替换为你想要保存的ICO文件路径

convert_png_to_ico(png_file, ico_file)


