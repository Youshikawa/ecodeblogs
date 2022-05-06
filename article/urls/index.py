from django.contrib import admin
from django.urls import path, include
from article.views.article_list import article_list
app_name = 'article'
urlpatterns = [
    path('articlelist/', article_list),
]