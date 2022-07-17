from django.http import HttpResponse
from django.http import JsonResponse
from blogs.models.blogs_user.blogs_user import Blogs_user
def getinfo(request):
    user = request.user # 当前网页的请求用户
    if not user.is_authenticated: # 如果改用户没有登录
        return JsonResponse({ # 那就返回未登入的状态
                "result":"unsuccess", 
            })
    else:
        blogs_user = Blogs_user.objects.get(user=user) # 找到与session中Default_user 对于的 Blogs_user.
        open_name = blogs_user.open_name
        if len(open_name) > 7 :
            open_name = open_name[:7] + "..."
        return JsonResponse({ # 返回登入的状态，并且返回这个Blogs_user 的各项信息
            "result":"success",
            "username":blogs_user.user.username,
           # "photo":blogs_user.photo,
            "uid": blogs_user.uid,
            "photo": blogs_user.photo.url,
            "open_name" : open_name, 
        })
