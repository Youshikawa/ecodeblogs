
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from mdeditor.fields import MDTextField

from ckeditor_uploader.fields import RichTextUploadingField 
# Create your models here.
class ArticlePost(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE)  ## 文章模型， 所属用户， 包含外键
    title = models.CharField(max_length=100) ### 文章标题
    # body = RichTextField() ### 文章内容
    # body = RichTextUploadingField(verbose_name="content")
    cover = models.ImageField(upload_to='blog_covers/%Y%m%d/',max_length=256,blank=True) # 文章展示图片，默认为通过外部链接或者内部静态链接导入
    body = MDTextField()
    created = models.DateTimeField(default=timezone.now) 
    updated = models.DateTimeField(auto_now=True)
    uid = models.CharField(max_length=100) ### 文章uid ， 随机生成
    catagories = models.CharField(max_length = 100, blank = True)
    @property
    def cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url
        else:
            return None
    class Meta:#    定义排序方式
        ordering = ('-created',)
    #获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail',args = [self.id])
    def __str__(self): # 定义显示内容
        return self.title