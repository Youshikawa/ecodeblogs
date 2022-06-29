from django.shortcuts import render
from article.models import ArticlePost
# 分页系统
from django.core.paginator import Paginator

from blogs.models.blogs_user.blogs_user import Blogs_user

def index(request):
    articles = ArticlePost.objects.all()
    # 每页文章数
    article_num = 5
    # 获取分页
    paginator = Paginator(articles, article_num)
    # 页码
    page = request.GET.get('page')
    # 获取当前页的文章
    getarticles = paginator.get_page(page)
    # context = { 'articles': articles }#旧版显示文章

    # 新版显示文章
    # 显示当前页面的文章
    context = {'articles' : getarticles,}
    return render(request, 'templates/main_page.html', context)