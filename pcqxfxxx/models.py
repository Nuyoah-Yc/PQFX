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