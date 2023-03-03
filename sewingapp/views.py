from django.shortcuts import render
from django.views import generic
from .models import PostPattern
from django.views.generic import ListView


class PostPattern(generic.ListView):
    model = PostPattern
    queryset = PostPattern.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    context_object_name = 'posted_patterns'