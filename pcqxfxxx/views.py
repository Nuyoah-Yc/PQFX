from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# 采集库
import requests
# 解析库
from bs4 import BeautifulSoup
# 时间库
import time
# 进度条库
from tqdm import tqdm
# 线程库
import threading
# Create your views here.

def pc(request):
    if request.method == 'GET':
        # 判断数据库是否有数据
        if url_name.objects.all():
            # 获取数据库中的前5条数据
            un1 = url_name.objects.order_by('id')[:5]
            nr1 = nr_list.objects.order_by('id')[:5]
            # 获取数据库中的后5条数据
            un2 = url_name.objects.order_by('-id')[:5]
            nr2 = nr_list.objects.order_by('-id')[:5]
            data = '有数据,清空再爬取'
            return render(request, 'pc.html', locals())
        else:
            data = '无数据,可以爬取了'
            return render(request, 'pc.html', locals())
    else:
        # 爬取异常处理
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
            }
            for page in tqdm(range(10)):
                url = 'https://movie.douban.com/top250?start={}&filter='.format(page * 25)
                response = requests.get(url=url, headers=headers)
                text = response.text
                soup = BeautifulSoup(text, 'html.parser')
                text_list = soup.select('ol.grid_view li div.info div.hd a')
                for line in text_list:
                    # 爬虫异常处理
                    try:
                        names_list = line.select('span.title')[0].text
                        urls_list = line.get('href')
                        print(names_list, urls_list)
                        # 保存到数据库url_name表
                        url_name.objects.create(name=names_list, url=urls_list)
                    except:
                        pass
            # 读取数据库url_name表的url数据
            url_list = url_name.objects.all()
            for url1 in tqdm(url_list):
                # 爬虫异常处理
                try:
                    response = requests.get(url=url1.url, headers=headers)
                    texts1 = response.text
                    soup1 = BeautifulSoup(texts1, 'html.parser')
                    # 获取电影播放时间
                    bf = soup1.select('div#content h1 span.year')[0].text
                    pl = soup1.select('div.mod-hd h2 span.pl a')[0].text
                    dz = soup1.select('div.rating_self strong.rating_num')[0].text
                    nr_list.objects.create(bf=bf, pl=pl, dz=dz)
                except:
                    pass
            # 获取数据库中的前5条数据
            un1 = url_name.objects.order_by('id')[:5]
            nr1 = nr_list.objects.order_by('id')[:5]
            # 获取数据库中的后5条数据
            un2 = url_name.objects.order_by('-id')[:5]
            nr2 = nr_list.objects.order_by('-id')[:5]
            data = '数据爬取成功'
            return render(request, 'pc.html', locals())
        except:
            data = '数据爬取失败'
            return render(request, 'pc.html', locals())
def qx(request):
    if request.method == 'GET':
        return render(request, 'qx.html')
    else:
        data = '数据清洗完成'
        return render(request, 'qx.html', locals())

def fx(request):
    if request.method == 'GET':
        return render(request, 'fx.html')
    else:
        data = '数据分析完成'
        return render(request, 'fx.html', locals())

def xx(request):
    if request.method == 'GET':
        return render(request, 'xx.html')
    else:
        data = '机器学习完成'
        return render(request, 'xx.html', locals())
