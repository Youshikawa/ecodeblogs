from django.urls import path, include 
from blogs.views.index import index
from blogs.views.user_info.user_info import user_info
urlpatterns = [

    ## 修改用户信息路由
    path("user_info/<str:uid>", user_info),
    path("user_info/", user_info),
    # --------* #

    path("", index, name = "main_page"),  # 当访问顶级路由时， 触发渲染主页面函数
    ## 登入路由
    path("login/", include('blogs.urls.login.index')),
    # ------* #
]