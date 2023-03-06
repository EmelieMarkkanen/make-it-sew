from . import views
from django.urls import path
from .views import PatternDetail, PostPattern, AllPatterns


urlpatterns = [
    path('', views.PostPattern.as_view(), name='index_page'),
    path('all_patterns/', views.AllPatterns.as_view(), name='all_patterns'),
    path('liked_patterns/', views.LikedPatterns.as_view(), name='liked_patterns'),
    path('<slug:slug>/', PatternDetail.as_view(), name='pattern_detail'),
]