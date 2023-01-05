from django.db import models

# Create your models here.

'''爬虫数据表'''
class url_name(models.Model):
    name = models.CharField(max_length=20, verbose_name='电影名称')
    url = models.CharField(max_length=100, verbose_name='电影地址')
    class Meta():
        db_table = 'url_name'
class nr_list(models.Model):
    bf = models.CharField(max_length=32, verbose_name='播放量')
    pl = models.CharField(max_length=32, verbose_name='评论量')
    dz = models.CharField(max_length=32, verbose_name='点赞量')
    class Meta():
        db_table = 'nr_list'


'''数据清洗表'''
class qx_list(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.CharField(max_length=20, verbose_name='年龄')
    height = models.CharField(max_length=20, verbose_name='身高')
    weight = models.CharField(max_length=20, verbose_name='体重')
    ip = models.CharField(max_length=20, verbose_name='ip地址')
    dq = models.CharField(max_length=20, verbose_name='地区')
    class Meta():
        db_table = 'qx_list'