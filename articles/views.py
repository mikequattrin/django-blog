# Article - App Views
from django.shortcuts import render
from django.http import Http404

from .models import Article

def index(request):
    return HttpResponse("Take me to the article listing page!")

def articles(request):
    article_list = Article.objects.order_by('-article_publication_date')[:5]
    return render(request, 'articles/articles.html', {'article_list': article_list})

def article(request, Article_id):
    try:
        article = Article.objects.get(pk=Article_id)
    except Article.DoesNotExist:
        raise Http404("Selected Article does not exist")
    return render(request, 'articles/article.html', {'article': article})
