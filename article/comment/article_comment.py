from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from article.models import ArticlePost
from blogs.models.blogs_user.blogs_user import Blogs_user
from .comment_models import Comment
from django.shortcuts import render, get_object_or_404, redirect
import markdown


def article_comment(request,uid):
    article = get_object_or_404(ArticlePost,id = uid)
    if request.method == 'POST':
        comment_from = CommentFrom(request.POST)
        if comment_from.is_valid():
            new_comment = 