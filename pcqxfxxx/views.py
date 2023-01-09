# 采集库
import requests
# 解析库
from bs4 import BeautifulSoup
# redis库
from django_redis import get_redis_connection
import redis
# 时间库
import time
# 进度条库
from tqdm import tqdm
# pandas库
import pandas as pd
# numpy库
import numpy as np
# os库
import os

from .models import *
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# 线程库
# Create your views here.



@csrf_exempt
def file_up(request):
    # 获取前端POST的文件数据
    file = request.FILES.get('file')
    file_name = time.strftime('%Y-%m-%d') + file.name
    # 保存文件到/file文件夹下
    with open('file/' + file_name, 'wb') as f:
        for line in file:
            f.write(line)
    # 判断file目录下文件是否存在
    if os.path.exists('file/' + file_name):
        data = {
            'text': '文件上传成功',
        }
        return JsonResponse(data)
    else:
        data = {
            'text': '文件上传失败',
        }
        return JsonResponse(data)

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
    if request.POST.get('id') == '1':
        # 数据集中存在字段缺失、空行、单位不统一、有重复数据等问题，请你使用NumPy和Pandas对数据进行清洗，具体要求如下：
        # 读取file文件夹下的mk2.xlsx文件
        df = pd.read_excel('file/mk2_list.xlsx')
        # 第一列为名字，第二列为年龄，第三列为身高，第三列为体重，第五列为ip，第六列为地区
        df.columns = ['name', 'age', 'height', 'weight', 'ip', 'area']

        # 1.缺失的体重和年龄字段使用均值填充，并且为整数
        df['age'] = df['age'].fillna(df['age'].mean()).astype(int)
        df['weight'] = df['weight'].fillna(df['weight'].mean()).astype(int)
        # 2.缺失的ip字段使用高频词填充；
        df['ip'] = df['ip'].fillna(df['ip'].mode()[0])
        # 3.身高单位统一为cm；
        # 查寻身高中有m或米的数据
        df1 = df[df['height'].str.contains('m|米')]
        print(df1)
        # 将身高单位的米和m去除
        # df['height'] = df['height'].str.replace('m', '').str.replace('米', '')
        # print(df)
        # 4.体重单位统一为kg；
        # 5.空行直接删除；
        # 6.重复数据只保留一条；
        # 7.将清洗后的数据通过DjangoORM保存到MySQL数据库中
        return JsonResponse({'text': '数据清洗完成'})



@csrf_exempt
def fx_Ajax(request):
        if request.POST.get('id') == '1':
            # 【任务1】读取所需数据集后，给用户数据中增加省份字段记录用户的归属地，分析该视频网站中会员用户在中国各地区的分布情况并绘制出会员分布图。绘图要求如下：
            # 1.使用PyEcharts库绘制会员分布地图；
            # 2.使用Django框架在前端页面中渲染展示会员分布图；
            # 【任务2】读取所需数据集后，分析不同类型的用户留存情况，并绘制用户留存矩阵图, 横轴为不同类型的用户留存率，纵轴为活跃用户的数量。绘图要求如下：
            # 1.使用PyEcharts库绘制留存矩阵图；
            # 2.使用Django框架在前端页面中渲染展示留存矩阵图
            pass


@csrf_exempt
def xx_Ajax(request):
    if request.POST.get('id') == '1':
        # [任务1]
        # 1.使用DjangoORM读取数据库中的用户日志数据；
        # 2.对数据进行清洗和处理，将处理后的数据保存为CSV数据；
        # 3.根据任务要求使用Pandas读取CSV数据进行特征工程；
        # 4.划分训练集和测试集；
        # 5.构建机器学习模型；
        # 6.编写模型训练相关代码，完成模型训练；
        # 7.使用PyEcharts库对测试数据的预测结果和真实结果进行可视化，并使用Django在前端页面中渲染展示；
        # 8.将训练好的模型保存。
        # [任务2]
        # 1.使用DjangoORM读取数据库中的广告收益数据进行数据清洗及处理；
        # 2.将清洗处理后的数据缓存到Redis数据库中；
        # 3.从Redis中读取数据进行特征工程；
        # 4.数据集划分；
        # 5.构建机器学习模型；
        # 6.编写模型训练相关代码，完成模型训练；
        # 7.使用PyEcharts库对测试数据的预测结果和真实结果进行可视化，并使用Django在前端页面中渲染展示；
        # 8.将训练好的模型保存。
        pass


@csrf_exempt
def text_Ajax(request):
    if request.POST.get('id') == '1':
        # 读取数据库url_name表的name列的数据
        # name_list = url_name.objects.values_list('name','url')
        # # 启用redis数据库
        # conn = get_redis_connection('default')
        # sj = conn.get('name_list')
        # sj = sj.decode('utf-8')
        # # conn.save()
        # for i in name_list:
        #     print(i[0],i[1])

        # keys = [key.decode() for key in conn.keys()]
        # # 显示所有的vlaue
        # for key in keys:
        #     print(key, conn.get(key).decode())
        from pyecharts import options as opts
        from pyecharts.charts import Map
        from pyecharts.faker import Faker

        c = (
            Map()
            .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
                visualmap_opts=opts.VisualMapOpts(max_=200),
            )
            .render("map_visualmap.html")
        )
        return HttpResponse(c)

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
    return render(request, 'qx.html', locals())


def fx(request):
    return render(request, 'fx.html')


def xx(request):
    if request.method == 'GET':
        return render(request, 'xx.html')
    else:
        data = '机器学习完成'
        return render(request, 'xx.html', locals())


def text(request):
    data = '文本处理完成'
    return render(request, 'text.html', locals())