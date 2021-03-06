from django.db import models
from django.contrib.auth.models import User
# 创建博客用户这个数据库模型，继承基本的数据库模型 (Django Default User)
class Blogs_user(models.Model): 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user_icon/%Y%m%d/',max_length=256,blank=True,default = '/media/user_icon/default/default.png') # 用户头像，默认为通过外部链接或者内部静态链接导入
    uid = models.CharField(default="",max_length=50,blank=True,null=True) # 用户的默认uid，随机生成
    open_name = models.CharField(default="",max_length=50,blank=True,null=True) # 用户的昵称, 字符串类型
    is_admin = models.BooleanField(default = False)
    about = models.CharField(default = "",max_length = 200,blank = True, null = False) # 简介
