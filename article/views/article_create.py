from django.http import HttpResponse
from article.views.forms import ArticlePostForm
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from article.models import ArticlePost
from django.db.models import Max
import math
import logging

#新建文章

def get_uid() :
    maxn = 0
    articles = ArticlePost.objects.all()
    for article in articles :
        maxn = max(int(article.uid), maxn)
    return maxn
def article_create(request):
    user = request.user
    if not user.is_authenticated: # 如果改用户没有登录
        return redirect('/login/')
    #判断用户是否提交表单数据
    if request.method == "POST" :
        #将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(request.POST,request.FILES)
        #判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit = False)
            #保存数据
            #保存数据到id为userid的用户
            new_article.author = user
            #获取文章uid值：最大的uid值+1
            data = ArticlePost.objects.all()
            '''
            for dt in data:
                temp = max(temp,int(dt.uid))
            '''
            temp = data.first().uid # 第一条uid：即最后插入的uid，保证为uid数据库中uid的最大值
            #print(temp)
            temp = str(int(temp) + 1)
            new_article.uid = str(temp)
            #new_article.uid = 'test'
            #保存文章
            article_post_form_cd = article_post_form.cleaned_data
            if 'cover' in request.FILES:
                new_article.cover = article_post_form_cd['cover']
            else:
                new_article.cover = 'blog_covers/default/type_blogs.png'
            new_article.catagories = article_post_form_cd['catagories']
            new_article.save()
            #返回文章列表
            #return redirect("/")
            return redirect('/article/detail/' + new_article.uid)
        else:
            #提交数据有误，返回当前界面
            article_post_form = ArticlePostForm()
            context = {'article_post_form':article_post_form}
            return redirect('templates/create/create.html',context)
    else:
        #创建表单类的实例
        article_post_form = ArticlePostForm()
        #赋值上下文
        context = {'article_post_form':article_post_form }
        #返回模板
        return render(request ,'templates/create/create.html', context)