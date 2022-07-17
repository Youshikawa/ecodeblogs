from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from article.models import ArticlePost
from blogs.models.blogs_user.blogs_user import Blogs_user
from comment.models import Comment
import markdown
from comment.forms import CommentForm

def article_detail(request, uid):
    articles = ArticlePost.objects.filter(uid = str(uid))
    if (len(articles) == 0) : return render(request,"templates/error/Not_found.html")
    article = articles[0]
    tag = article.catagories
    users = Blogs_user.objects.filter(user = article.author)
    if (len(users) == 0) : return render(request,'templates/error/Not_found.html')
    user = users[0]
    if (len(user.open_name) > 7) : user.open_name = user.open_name[:7] + '...'
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
    comments = Comment.objects.filter(article=article)
    comment_form = CommentForm()
    if (len(articles) > 0) :
        delete = ""
        updated = ""
        if (article.author == request.user) :
            delete = " <a onclick=\"confirm_delete()\" class = \"delete_btn\" ><img class = \"delete_ico\"src = \"/static/image/article_del/article_del1.png\"> </a>"
            updated = "<a onclick=\"location.href='/article/article_update/"+uid+"'\" class = \"update_btn\" > <img class = \"update_ico\"src = \"/static/image/article_edit/article_edit1.png\"> </a>"
        comments = comments[::-1]
        context = {'article':article,
                    'user' : user, 
                    'delete':delete,
                    'updated':updated,
                    'toc':md.toc,
                    'comments':comments,
                    'comment_form':comment_form,
                    'catagories':tag
        }
        return render(request, 'templates/article/article.html', context)
    return render(request,"templates/error/Not_found.html")