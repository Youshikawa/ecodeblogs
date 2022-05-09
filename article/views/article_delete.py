from .article_list import article_list
from article.models import ArticlePost
from django.shortcuts import render , resirect
from django.contrib.auth.models import User
from django.http import HttpResponse

#删除文章

def article_delete(request , article_id , user_id):
    #获取uid删除文章
    article = ArticlePost.objects.get(id = article_id)
    #获取当前文章的用户uid
    userUID = article.author
    if user_id == userUID or user_id == 0:
        article.delete()
        return redirect('article:article_list')
    else :
        #如果用户uid和文章的作者不一致，则不允许删除
        return HttpResponse("ERROR:You can't delete this passage")