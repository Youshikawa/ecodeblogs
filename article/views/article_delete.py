from .article_list import article_list
from article.models import ArticlePost
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from blogs.models.blogs_user.blogs_user import Blogs_user
#删除文章

def article_delete(request , uid):
    if request.method != 'POST': return HttpResponse("<a style=\"font-size : 30px\">404 Bad")
    user = request.user
    users = Blogs_user.objects.filter(user=user)
    if (users.exists() == False) : return False
    blogs_user = users[0]
    #获取uid删除文章
    articles = ArticlePost.objects.filter(uid = uid)
    if articles.exists() == False : return HttpResponse("ERROR:Article already deleted")
    article = articles[0]
    #获取当前文章的用户uid
    userUID = article.author
    if request.user == article.author or user.is_admin:
        article.delete()
        return redirect('/')
    else :
        #如果用户uid和文章的作者不一致，则不允许删除
        return HttpResponse("ERROR:You can't delete this passage")
