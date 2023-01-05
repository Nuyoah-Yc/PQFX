# 采集库
import requests
# 解析库
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# 时间库
# 进度条库
from tqdm import tqdm

from .models import *


# 线程库
# Create your views here.


@csrf_exempt
def pc_Ajax(request):
    # 获取前端POST请求的数据
    vlus = request.POST.get('id')
    if vlus == '1':
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
                try:
                    names_list = line.select('span.title')[0].text
                except:
                    names_list = ''
                try:
                    urls_list = line.get('href')
                except:
                    urls_list = ''
                url_name.objects.create(name=names_list, url=urls_list)
        # 读取数据库url_name表的url数据
        url_list = url_name.objects.all()
        for url1 in tqdm(url_list):
            response = requests.get(url=url1.url, headers=headers)
            texts1 = response.text
            soup1 = BeautifulSoup(texts1, 'html.parser')
            try:
                bf = soup1.select('div#content h1 span.year')[0].text
            except:
                bf = ''
            try:
                pl = soup1.select('div.mod-hd h2 span.pl a')[0].text
            except:
                pl = ''
            try:
                dz = soup1.select('div.rating_self strong.rating_num')[0].text
            except:
                dz = ''
            nr_list.objects.create(bf=bf, pl=pl, dz=dz)
        data = {
            'text': '数据爬取完成',
        }
        return JsonResponse(data)
    elif vlus == '2':
        if url_name.objects.all():
            # 清空数据库
            url_name.objects.all().delete()
            nr_list.objects.all().delete()
            data = {
                'text': '数据清空完成',
            }
            return JsonResponse(data)
        else:
            data = {
                'text': '数据库无数据',
            }
            return JsonResponse(data)


@csrf_exempt
def qx_Ajax(request):
    pass


@csrf_exempt
def fx_Ajax(request):
    pass


@csrf_exempt
def xx_Ajax(request):
    pass


@csrf_exempt
def text_Ajax(request):
    pass



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


def text(request):
    return render(request, 'text.html')
