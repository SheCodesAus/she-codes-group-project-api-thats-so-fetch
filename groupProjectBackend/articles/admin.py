from django.contrib import admin
from .models import Articles, Category, Comment

# # Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'author']
    class Meta:
        model = Articles

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'slug']


# class ArticlesAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'description', 'goal', 'category', 'date_created']

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['comment', 'anonymous', 'articles'] 

# admin.site.register(Comment, CommentAdmin)







