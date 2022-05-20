from django.contrib import admin
from django.urls import path, include
from article.views.article_list import article_list
from article.views.article_detail import article_detail
from article.views.article_create import article_create
app_name = 'article'
urlpatterns = [
    path('article_create/', article_create),
    path('detail/<str:uid>', article_detail, name = "article_detail"),
    path('articlelist/', article_list),
]