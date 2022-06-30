from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost
from ckeditor.fields import RichTextField


#评论的模型
class Comment(models.Model):
    article = models.ForeignKey(ArticlePost,on_delete = models.CASCADE,related_name = 'comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'comments')
    body = RichTextField()
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ('created',)
    def __srt__(self):
        return self.body
# Create your models here.
