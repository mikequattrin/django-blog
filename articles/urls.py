from django.conf.urls import url

from . import views

urlpatterns = [

    # Articles Listing Page
    url(r'^$', views.articles, name='articles'),

    # Individual Article Page
    url(r'^/(?P<Article_id>[0-9]+)/$', views.article, name='article'),
]