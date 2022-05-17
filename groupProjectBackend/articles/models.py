from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    # goal_date = models.DateTimeField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
        )

    category = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='project_id'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    articals = models.ForeignKey(
        'Articles',
        on_delete=models.CASCADE,
        related_name='Comment'
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
