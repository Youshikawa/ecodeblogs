
from blogs.views.user_info.forms import BlogsUserForm
from django.shortcuts import render, redirect
from blogs.models.blogs_user.blogs_user import Blogs_user             
from django.http import JsonResponse
from django.contrib.auth import authenticate,logout

def user_info(request, uid = ""):
    user = request.user
    if not user.is_authenticated: # 如果改用户没有登录
        return redirect('/login/')
    blogs_users = Blogs_user.objects.filter(uid = uid)
    if blogs_users.exists() == False: return JsonResponse({"result":"user_is_not_exist",})
    blogs_user = blogs_users[0]
    user_request = blogs_user.user
    if request.method == 'POST':
        if user != user_request:
            return JsonResponse({"result":"invalid_opr",})
        blogs_user_form = BlogsUserForm(request.POST, request.FILES)
        if blogs_user_form.is_valid():
            blogs_user_cd = blogs_user_form.cleaned_data
            blogs_user.open_name = blogs_user_cd["open_name"]
            blogs_user.about = blogs_user_cd['about']
            if 'photo' in request.FILES:
                blogs_user.photo = blogs_user_cd["photo"]
            # .....
            blogs_user.save()
            return redirect("/")
        else:
            return JsonResponse({"result":"faild",})
    elif request.method == "GET" :
        blogs_user_form = BlogsUserForm()
        context = {"blogs_user_form" : blogs_user_form, "blogs_user":blogs_user, "user":user}
        return render(request,"templates/user_info/user_info.html" , context)