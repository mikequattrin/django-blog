# Article - App Views
from django.shortcuts import render
from django.http import Http404

from .models import Article

def articles(request):
    articles_random = Article.objects.order_by('?')[:4]
    article_list = Article.objects.order_by('article_publication_date')[:3]
    return render(request, 'articles/articles.html', {
        'article_list': article_list, 
        'articles_random': articles_random,
        })

def article(request, Article_id):
    try:
        article = Article.objects.get(pk=Article_id)
        articles_random = Article.objects.order_by('?')[:4]
    except Article.DoesNotExist:
        raise Http404("Selected Article does not exist")
    return render(request, 'articles/article.html', {
        'article': article,
        'articles_random': articles_random,
        })

