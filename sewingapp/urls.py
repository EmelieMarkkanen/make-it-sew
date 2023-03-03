from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostPattern.as_view(), name='home'),
]