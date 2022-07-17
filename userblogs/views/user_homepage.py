from django.shortcuts import render, redirect
from article.models import ArticlePost
# 分页系统
from django.core.paginator import Paginator

from blogs.models.blogs_user.blogs_user import Blogs_user
def get_catagories(articles):
    s = set()
    for article in articles : 
        s.add(article.catagories)
    return list(s)
    
def index(request, uid, category) :
    blogs_users = Blogs_user.objects.filter(uid = uid)
    if blogs_users.exists() == False : return redirect('/')
    blogs_user = blogs_users[0]
    user = blogs_user.user
    articles = ArticlePost.objects.filter(author = user)
    catagories = get_catagories(articles)
    # 每页文章数
    article_num = 8
    # 获取分页
    paginator = Paginator(articles, article_num)
    # 页码
    page = request.GET.get('page')
    # 获取当前页的文章
    getarticles = paginator.get_page(page)

    if (len(blogs_user.open_name) > 10) : blogs_user.open_name = blogs_user.open_name[:9] + '...'
    context = {'articles' : getarticles,
                'user' : blogs_user,
                'catagories':catagories,
                'category' : category,
        }
    return render(request, 'templates/user_homepage/user_homepage.html'
    , context)