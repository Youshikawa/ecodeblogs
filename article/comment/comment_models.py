from django.db import models
from django.contrib.auth.models import User
from models import ArticlePost


#评论的模型
class Comment(models.Model):
    article = models.ForeignKey(ArticlePost,on_delete = models.CASCADE,related_name = 'comments')
    user = models.models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'comments')
    body = models.TextField()
    created = models.DateTineField(auto_new_add = True)
    class Meta:
        ordering = ('created',)
    def __srt__(self):
        return self.body