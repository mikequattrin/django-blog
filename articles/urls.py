from django.conf.urls import url

from . import views

urlpatterns = [
    # Homepage
    url(r'^$',views.index, name='index'),

    # Articles Listing Page
    url(r'^articles/$', views.articles, name='articles'),

    # Individual Article Page
    url(r'^articles/(?P<Article_id>[0-9]+)/$', views.article, name='article'),
]