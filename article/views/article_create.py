from django.http import HttpResponse
from .froms import ArticlePostForm
from django.shortcuts import render , resirect



#新建文章


def article_create(request):
    #判断用户是否提交表单数据
    if request.method == "POST" :
        #将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data = request.POST)
        #判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit = False)
            #保存数据
            