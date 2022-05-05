from django.urls import path, include 
from blogs.views.login.index import index
urlpatterns = [
    path('getinfo/', include('blogs.urls.login.getinfo.index')),
   path("", index, name = "login"),  # 当访问顶级路由时， 触发渲染主页面函数
    
]