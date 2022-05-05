from django.urls import path, include 
from blogs.views.login.getinfo.getinfo import getinfo
urlpatterns = [
    path('', getinfo, name = "getinfo"), # 获取登录信息
]