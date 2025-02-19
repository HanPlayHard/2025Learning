from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""

    text = models.CharField(max_length=200)  # CharField——由字符组成的数据，即文本
    date_added = models.DateTimeField(auto_now_add=True)  # 记录日期和时间的数据

    def __str__(self):
        """返回模型的字符串表示"""
        # 每当需要生成 表示模型实例 的输出时，Django 都将调用这个方法
        return self.text
