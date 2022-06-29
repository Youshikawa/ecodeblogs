from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from article.models import ArticlePost
from blogs.models.blogs_user.blogs_user import Blogs_user
from .comment_models import Comment
import markdown

def article_detail(request, uid):
    articles = ArticlePost.objects.filter(uid = str(uid))
    if (len(articles) == 0) : return HttpResponse("404 Not Found")
    article = articles[0]
    users = Blogs_user.objects.filter(user = article.author)
    if (len(users) == 0) : return HttpResponse("404 Not Found")
    user = users[0]
    md = markdown.Markdown(
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        # 文章目录拓展
        'markdown.extensions.toc',
        ])
    article.body = md.convert(article.body)
    comments = Comment.objects.filter(article=uid)
    if (len(articles) > 0) :
        delete = ""
        updated = ""
        if (article.author == request.user) :
            delete = " <a onclick=\"confirm_delete()\" ><button style = \"top:8% ;font-size:100%;right: 16%;\" class=\"btn-delete\"> - Delete </button> </a>"
            updated = "<a onclick=\"location.href='/article/article_update/"+uid+"'\" ><button style = \"top:8% ;font-size:100%;right: 10%;\" class=\"btn-up\">  { Update </button> </a>"
        context = {'article':article,
                    'user' : user, 
                    'delete':delete,
                    'updated':updated,
                    'toc':md.toc,
                    'comments':comments,
        }
        return render(request, 'templates/article/article.html', context)
    return JosnResponse("sorry, no such article.")