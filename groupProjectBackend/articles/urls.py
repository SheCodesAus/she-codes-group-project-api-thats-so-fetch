from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
   
    path('articles/', views.ArticlesList.as_view()),
    path('articles/<int:pk>/', views.ArticlesDetail.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category'),
    path("comments/", views.CommentList.as_view(),name='comment_list'),

    # path("comments/", views.CommentList.as_view(),name='comment_list'),
 
]

urlpatterns = format_suffix_patterns(urlpatterns)