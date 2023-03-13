from . import views
from django.urls import path, include
from .views import PatternDetail, PostPattern, AllPatterns, EditPattern, PP, PatternLike

urlpatterns = [
    path('', views.PostPattern.as_view(), name='index'),
    path('all_patterns/', views.AllPatterns.as_view(), name='all_patterns'),
    path('liked_patterns/', views.LikedPatterns.as_view(), name='liked_patterns'),
    path('my_patterns/', views.MyPatterns.as_view(), name='my_patterns'),
    path('post_pattern/', views.PostPatternForm.as_view(), name='post_pattern'),
    path('accounts/', include('allauth.urls')),
    path('edit_pattern/<slug:slug>/', views.EditPattern.as_view(), name='edit_pattern'),
    path('like/<slug:slug>/', views.PatternLike.as_view(), name='pattern_like'),
    path('<slug:slug>/', views.PatternDetail.as_view(), name='pattern_detail'),
]