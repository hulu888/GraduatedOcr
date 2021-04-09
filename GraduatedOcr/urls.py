"""GraduatedOcr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from views import recog_view, user, img_manager

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recognition/', recog_view.recognition),
    re_path('^$', user.login),
    path('login/', user.login),
    path('index/', recog_view.index),
    path('usersmanage/', user.usersmanage),
    path('imagesmanage/', img_manager.imagesmanage),
    # path('form/', recog_view.form),
    path('chart/', recog_view.chart),
    path('404/', recog_view.not_found),
    path('register/', user.register),

    path('adduser/', user.adduser),
    re_path('^edituser', user.edituser),

]












