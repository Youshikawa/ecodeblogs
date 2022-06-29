from django import forms
from .comment_models import Comment

class CommentFrom(froms.ModelFrom):
    class Meta:
        model = Comment
        fields = ['body']