from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CustomUserList.as_view()),
    # path('<int:pk>/', views.CustomUserDetail.as_view()),
    path('register/', views.CustomUserList.as_view()),
    path('login/', views.CustomUserList.as_view()),
    path('profile/<int:pk>/', views.CustomUserDetail.as_view()),
# to delete "user" from path otherwise it is user/user/register for example
]

urlpatterns = format_suffix_patterns(urlpatterns)
