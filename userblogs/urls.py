from django.urls import path
from .views.user_homepage import index as user_homepage


urlpatterns = [
    path('homepage/<str:uid>/<str:category>/', user_homepage, name = "user_homepage"),
    # 个人主业
]