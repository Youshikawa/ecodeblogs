
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class ArticlePost(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE)  ## 文章模型， 所属用户， 包含外键
    title = models.CharField(max_length=100) ### 文章标题
    body = models.TextField()  ### 文章内容
    created = models.DateTimeField(default=timezone.now) 
    updated = models.DateTimeField(auto_now=True)
    uid = models.CharField(max_length=100) ### 文章uid ， 随机生成
    class Meta:#    定义排序方式
        ordering = ('-created',)

    def __str__(self): # 定义显示内容
        return self.title