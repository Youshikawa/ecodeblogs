
from django.shortcuts import render

# 导入数据模型ArticlePost
from article.models import ArticlePost
# 分页系统
from django.core.paginator import Paginator

def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    # 每页文章数
    article_num = 2
    # 获取分页
    paginator = Paginator(articles, article_num)
    # 页码
    page = request.GET.get('page')
    # 获取当前页的文章
    getarticles = paginator.get_page(page)
    # context = { 'articles': articles }#旧版显示文章

    # 新版显示文章
    # 显示当前页面的文章
    context = {'articles' : getarticles}

    # render函数：载入模板，并返回context对象
    context = {article : "article"}
    return render(request, 'templates/list.html', context) 