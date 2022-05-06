from django.shortcuts import render
from article.models import ArticlePost
def index(request):
    articles = ArticlePost.objects.all()
    context = {'articles' : articles}
    return render(request, 'templates/main_page.html', context)