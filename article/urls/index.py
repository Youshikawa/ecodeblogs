from django.contrib import admin
from django.urls import path, include
from article.views.article_list import article_list
from article.views.article_detail import article_detail
from article.views.article_create import article_create
from article.views.article_delete import article_delete
from article.views.article_update import article_update
app_name = 'article'
urlpatterns = [
    path('article_create/', article_create),
    path('detail/<str:uid>', article_detail, name = "article_detail"),
    path('articlelist/', article_list),
    path('article_delete/<int:uid>', article_delete),
    path('article_update/<str:uid>', article_update),
]