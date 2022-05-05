from django.urls import path, include 
from blogs.views.index import index
urlpatterns = [
    path("", index, name = "main_page"),  # 当访问顶级路由时， 触发渲染主页面函数
    path("login/", include('blogs.urls.login.index')),
]