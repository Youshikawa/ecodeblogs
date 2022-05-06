from django.urls import path, include 
from blogs.views.login.index import index as login
from blogs.views.logout.index import index as logout
urlpatterns = [
    path('getinfo/', include('blogs.urls.login.getinfo.index')),
    path('logout/', logout),# 登出路由
    path("", login, name = "login"),  # 当访问顶级路由时， 触发渲染主页面函数
]