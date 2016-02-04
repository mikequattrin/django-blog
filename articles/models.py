# Article Models
from django.db import models


class Article(models.Model):
    article_text = models.CharField(max_length=200, default = '')
    article_author = models.CharField(max_length=200, default = '')
    article_publication_date = models.DateTimeField('date published')
    article_category = models.CharField(max_length=200, default = '')
    article_hero_image = models.ImageField(upload_to='images/%Y/%m/%d')
    article_optional_image = models.ImageField(upload_to='images/%Y/%m/%d')
    article_body_text = models.TextField(default = '')

    def __str__(self):
        return self.article_text