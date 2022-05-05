from django.db import models
from django.contrib.auth.models import User
# 创建博客用户这个数据库模型，继承基本的数据库模型 (Django Default User)
class Blogs_user(models.Model): 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.URLField(max_length=256,blank=True) # 用户头像，默认为通过外部链接或者内部静态链接导入
    uid = models.CharField(default="",max_length=50,blank=True,null=True) # 用户的默认uid，随机生成
    open_name = models.CharField(default="",max_length=50,blank=True,null=True) # 用户的昵称, 字符串类型
