from django.http import HttpResponse
from .froms import ArticlePostForm
from django.shortcuts import render , resirect
from django.contrib.auth.models import User
from article.models import ArticlePost
import math

#新建文章


def article_create(request,userid):
    #判断用户是否提交表单数据
    if request.method == "POST" :
        #将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data = request.POST)
        #判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit = False)
            #保存数据
            #保存数据到id为userid的用户
            new_article.author = User.objects.get(uid = userid)
            #获取文章uid值：最大的uid值+1
            new_article.uid = str(Math.max(article.objects.all(), key = uid) + 1)
            #保存文章
            new_article.save()
            #返回文章列表
            return redirect("article:article_list")
        else:
            #提交数据有误，输出ERROR
            return HttpResponse("Submit EEROR!")
    else:
        #创建表单类的实例
        article_post_form = ArticlePostForm()
        #赋值上下文
        context = {'article_post_form':article_post_form }
        #返回模板
        return render(request ,'templates/create/create.html', context)