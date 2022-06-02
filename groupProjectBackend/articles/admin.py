from django.contrib import admin
from .models import Articles, Comment

# # Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'content',
    'image', 'owner']

admin.site.register(Articles, ArticlesAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'anonymous', 'articles', 'supporter'] 

admin.site.register(Comment, CommentAdmin)







