from django.http import JsonResponse
from django.contrib.auth import authenticate,login
def signin(request) :
    data = request.GET # 获得请求的数据
    username = data.get("username")
    password = data.get("password")
    user = authenticate(username = username, password = password) ## 找到对应的user
    if not user : ##    用户不存在， 说明用户密码错误
        return JsonResponse({
            "result" : "unsuccess" ,
        })
    else :  ##          登录成功
        login(request, user)
        return JsonResponse({
            "result" : "success" ,
        })