from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CustomUserList.as_view()),
    # path('<int:pk>/', views.CustomUserDetail.as_view()),
    path('user/register/', views.RegisterView.as_view()),
    path('login/', views.CustomUserList.as_view()),
    path('user/profile-page/<str:username>/', views.CustomUserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
