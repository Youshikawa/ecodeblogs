from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from random import randint
from blogs.models.blogs_user.blogs_user import Blogs_user
def check(pswd) : 
    ans = 1
    if len(pswd) < 8 :
        return 1
    for c in pswd :
        if c < '0' or c > '9' :
            return 0
    return 1

def create_uid() : #  生成uid
    uid = User.objects.all().count()
    return str(uid)

def register(request) :
    data = request.GET
    username = data.get("username", "").strip() # strip()移除首位空格 而且如果参数没有提交，返回一个空的字符串
    password = data.get("password", "").strip() # 密码 而且如果参数没有提交，返回一个空的字符串
    password_confirm = data.get("password_confirm", "").strip()# 同理 ^
    if not username or not password : # 用户名密码， 不嫩为空
        return JsonResponse({
            "result" : "info_null", 
        })
    if password != password_confirm : ## 确认密码与密码不一致
        return JsonResponse({
            "result" : "password_confirm_error" ,
        })
    if User.objects.filter(username=username).exists(): ## 用户名已村在
        return JsonResponse({
            "result" : "username_exist" ,
        })
    if check(password) :                                   ## 密码强度不够
        return JsonResponse({
             "result" : "password_not_allowed",
        })
    user = User(username = username) ##         调用构造函数，新建用户
    user.set_password(password)
    user.save()
    uid = create_uid()
    Blogs_user.objects.create(user = user, photo = "https://tse1-mm.cn.bing.net/th/id/R-C.261fd27312a8586ced2c7f86af61e6cc?rik=kc%2b30zH5arnQ7g&riu=http%3a%2f%2fpic2.52pk.com%2ffiles%2f131026%2f1285603_150529_1.jpg&ehk=UnpVJNkvqUhG1lt4IxOEHRd1hnAhw%2fdwecDUmoKHJsw%3d&risl=&pid=ImgRaw&r=0", uid = uid, open_name = username)
    login(request, user)
    return JsonResponse({
        "result" : "success" ,
    })