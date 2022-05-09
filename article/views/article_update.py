from .article_list import article_list
from article.models import ArticlePost
from django.shortcuts import render , resirect
from django.contrib.auth.models import User
from django.http import HttpResponse

#更新文章
#article_id为文章id，user_id是用户id
def article_update(request, article_id, user_id):
    #获取id为article_id的文章
    article = ArticlePost.objects.get(id = article_id)
    userUID = article.author
    #如果不是管理员或者文章作者来修改文章，则不允许修改
    if user_id != 0 and userUID != user_id:
        return HttpResponse("ERROR:You can't update this passage")
    if request.method == "POST" :
        article_post_form = ArticlePostForm(data  = request.POST)
        #判断文章是否符合模型需求
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = redirect.post['body']
            article.save()
            return redirect('article:article_list',id = article_id)
        else:
            return HttpResponse("submit ERROR!")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        return redirect(request, 'templates/update/update.html',context)
