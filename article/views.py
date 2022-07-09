from django.shortcuts import render


def article_home_view(request):
    return render(request, 'article/article-index-view/index.html')

def open_article_view(request):
    pass