from django.http import JsonResponse
from django.contrib.auth import authenticate,logout
from django.shortcuts import redirect
def index(request) :
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'result': "success"
        })
    logout(request) # 退出登录
    return redirect("/")