from . import views
from django.urls import path, include
from .views import PatternDetail, PostPattern, AllPatterns


urlpatterns = [
    path('', views.PostPattern.as_view(), name='index'),
    path('all_patterns/', views.AllPatterns.as_view(), name='all_patterns'),
    path('liked_patterns/', views.LikedPatterns.as_view(), name='liked_patterns'),
    path('accounts/', include('allauth.urls')),
    path('<slug:slug>/', PatternDetail.as_view(), name='pattern_detail'),
]