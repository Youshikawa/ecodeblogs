from django.http import JsonResponse
from django.contrib.auth import authenticate,logout
def index(request) :
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'result': "success"
        })
    logout(request) # 退出登录
    return JsonResponse({
        'result' : 'success'
    })