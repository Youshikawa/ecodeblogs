from django.urls import path, include 
from blogs.views.login.index import index as login
from blogs.views.logout.index import index as logout
from blogs.views.login.register import register
from blogs.views.login.signin import signin
urlpatterns = [
    path('register', register),
    path('getinfo/', include('blogs.urls.login.getinfo.index')),
    path('signin/', signin),
    path('logout/', logout),# 登出路由
    path("", login, name = "login"),  # 当访问顶级路由时， 触发渲染主页面函数
]