"""Vaughan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from blog import views as blog_views
from background import views as background_views
urlpatterns = [
    path('',blog_views.index,name='index'),
    path('signup/',background_views.singup,name='signup'),
    path('signin/',background_views.signin,name='signin'),
    path('details/',blog_views.detail,name='details'),
    path('test/',background_views.test),
    path('admin/',background_views.admin),
    path('profile/',background_views.profile),
    path('table/',background_views.table),
    path('article/',background_views.article),
    path('login/',background_views.login),
    path('register/',background_views.register),

]
