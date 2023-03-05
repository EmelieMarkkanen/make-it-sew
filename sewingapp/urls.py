from . import views
from django.urls import path
from .views import PatternDetail, PostPattern


urlpatterns = [
    path('', views.PostPattern.as_view(), name='index_page'),
    path('<slug:slug>/', PatternDetail.as_view(), name='pattern_detail'),
]