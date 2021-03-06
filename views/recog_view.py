from django.http import HttpResponse
from django.shortcuts import redirect, render
import time
import json
from django.contrib.auth.models import User

from . import recognition as recog


def index(request):
    if request.method == 'GET':
        return render(request, 'ocr/index.html')


def form(request):
    if request.method == 'GET':
        return render(request, 'ocr/recognition.html')


def chart(request):
    if request.method == 'GET':
        return render(request, 'ocr/chart.html')


def not_found(request):
    if request.method == 'GET':
        return render(request, 'ocr/404.html')


def recognition(request):
    if request.method == 'GET':
        return render(request, 'ocr/recognition.html')

    if request.method == 'POST':

        # 获取图片对象
        img_obj = request.FILES.get('img')
        # 构造文件名以及文件路径
        img_name = './static/UploadImages/' + img_obj.name.split('.')[0] + '_' + str(int(time.time())) + '.' + \
                   img_obj.name.split('.')[-1]
        # 保存图片
        with open(img_name, 'wb+') as f:
            f.write(img_obj.read())

        reg_images = [img_name]
        start = time.time()
        results = recog.reg_image(reg_images)
        end = time.time()
        print(end - start)
        if results:
            reg_data = results[0]
            return HttpResponse(json.dumps(reg_data))
        else:
            reg_data = 'false'
            return HttpResponse(reg_data)
