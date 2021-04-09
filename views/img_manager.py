from django.shortcuts import redirect, render
from django.http import HttpResponse
import os


def imagesmanage(request):
    if request.method == 'GET':
        for path, _, files in os.walk('static/UploadImages'):
            pass
        return render(request, 'img_manage/imagesmanage.html', context={'files': files, 'path': path})