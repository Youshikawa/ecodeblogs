from .article_list import article_list
from article.models import ArticlePost
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from article.views.forms import ArticlePostForm

#更新文章
#article_id为文章id，user_id是用户id
def article_update(request, uid):
    article_id = str(uid)
    user = request.user
    if not user.is_authenticated: # 如果改用户没有登录
        return redirect('/login/')
    #获取id为article_id的文章
    #article = ArticlePost.objects.get(id = article_id)
    article = ArticlePost.objects.filter(uid = str(uid))[0]
    userUID = article.author
    #如果不是管理员或者文章作者来修改文章，则不允许修改
    if userUID != user:
        return HttpResponse("ERROR:You can't update this passage")
    if request.method == "POST" :
        article_post_form = ArticlePostForm(data  = request.POST)
        #判断文章是否符合模型需求
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect('/article/detail/' + article_id)
        else:
            return HttpResponse("submit ERROR!")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        #context = {'article_post_form': article_post_form }
        #return redirect(request, 'templates/update/update.html',context)
        return render(request, 'templates/update/update.html',context)
