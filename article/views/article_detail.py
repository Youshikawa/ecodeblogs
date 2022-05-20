from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from article.models import ArticlePost
import markdown

def article_detail(request, uid):
    articles = ArticlePost.objects.filter(uid = str(uid))
    article = articles[0]
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    if (len(articles) > 0) :
        
        context = {'article':article}
        return render(request, 'templates/article/article.html', context)
    return JosnResponse("sorry, no such article.")