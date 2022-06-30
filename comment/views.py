from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from article.models import ArticlePost
from blogs.models.blogs_user.blogs_user import Blogs_user
from .forms import CommentForm
from .models import Comment
from django.shortcuts import render, get_object_or_404, redirect
import markdown


# 文章评论

def article_comment(request,uid):
    article = get_object_or_404(ArticlePost,uid = uid)
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        comment_from = CommentForm(request.POST)
        if comment_from.is_valid():
            new_comment = comment_from.save(commit = False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect('/article/detail/' + article.uid)
        else:
            return redirect('/article/detail/' + article.uid)
    else:
        return HttpResponse("You can only POST the comment!!!")
# Create your views here.
