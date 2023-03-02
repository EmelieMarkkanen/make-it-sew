from django.shortcuts import render
from django.views import generic
from .models import PostPattern


class PostPattern(generic.ListView):
    model = PostPattern
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
