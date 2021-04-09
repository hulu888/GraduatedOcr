from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
from django.core import serializers
import json


def register(request):

    # create()创建用户，密码为明文
    # create_user()创建用户，密码为密文
    # create_superuser()创建超级用户，密码为密文，需要多传一个邮箱参数
    User.objects.create_user(username='zhangr', password='keen321.')
    return 'success'


def login(request):
    if request.method == 'GET':
        return render(request, 'ocr/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = auth.authenticate(username=username, password=password)

        if not user_obj:
            msg = 'failed'

        else:
            msg = 'success'
        return HttpResponse(msg)


def usersmanage(request):
    if request.method == 'GET':
        # 获取所有用户信息

        user_data = {'users': User.objects.all()}
        return render(request, 'user/usersmanage.html', context=user_data)

    if request.method == 'DELETE':
        data = QueryDict(request.body)
        user_id = data.get('userId')
        res = User.objects.filter(id=user_id).delete()

        if res:

            msg = 'success'
        else:
            msg = 'failed'
        return HttpResponse(msg)


def adduser(request):
    if request.method == 'GET':

        return render(request, 'user/adduser.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        manager = request.POST.get('manager')
        email = request.POST.get('email')
        if manager == 'true':
            User.objects.create_superuser(username=username, password=password, email=email)
        else:
            User.objects.create_user(username=username, password=password, email=email)
        return redirect('/usersmanage/')


def edituser(request):
    if request.method == 'GET':
        user_id = request.GET.get('id')
        user_json = serializers.serialize('json', User.objects.filter(id=user_id))
        user = json.loads(user_json)[0].get('fields')
        # if user:
        user['id'] = user_id
        user_data = {'user': user}
        return render(request, 'user/edituser.html', context=user_data)
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        manager = request.POST.get('manager')
        user_id = request.POST.get('userId')

        User.objects.filter(id=user_id).update(username=username, email=email, is_staff=manager.capitalize())
        if password:

            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.save()

        return redirect('/usersmanage/')

