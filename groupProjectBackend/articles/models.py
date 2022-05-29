from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.category

class Articles(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.CharField(max_length=300)
    image = models.URLField()
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE, related_name='author_articles')
    category = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='articles',
        related_query_name='articles'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    articles = models.ForeignKey(
        'Articles',
        on_delete=models.CASCADE,
        related_name='comment'
    )
    # supporter =models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_comment'
        )


