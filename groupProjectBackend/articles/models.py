from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.CharField(max_length=6000)
    image = models.URLField()
    owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='owner_articles'
    )
    # commenting categories out because it is a class
    # category = models.ForeignKey(
    #     'Category',
    #     null=True, blank=True,
    #     on_delete=models.CASCADE,
    #     related_name='article_id'
    # )

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


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.title



# class Comment(models.Model):
#     message = models.CharField(max_length=200)
#     anonymous = models.BooleanField()
#     articles = models.ForeignKey(
#         'Articles',
#         on_delete=models.CASCADE,
#         related_name='Comment'
#     )
#     commenter = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
#         related_name='comments'
#         )
