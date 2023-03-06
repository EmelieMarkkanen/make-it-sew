from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator
from .models import PostPattern
from .models import PostPattern as PP
from django.views.generic import ListView


class PostPattern(generic.ListView):
    model = PostPattern
    queryset = PostPattern.objects.filter(status=1, featured_pattern=True).order_by("-created_on")
    template_name = "index.html"
    context_object_name = 'posted_patterns'


class PatternDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = PP.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        page = 'pattern_detail'
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "pattern_detail.html",
            {
                "post": post,
                "page": page,
                "liked": liked,
            },
        )


class AllPatterns(generic.ListView):

    model = PostPattern
    queryset = PP.objects.filter(status=1).order_by('-created_on')
    template_name = "all_patterns.html"
    paginate_by = 9
    context_object_name = 'posted_patterns'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'all_patterns'
        return context