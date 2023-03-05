from django.shortcuts import render
from django.views import generic
from .models import PostPattern
from django.views.generic import ListView


class PostPattern(generic.ListView):
    model = PostPattern
    queryset = PostPattern.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    context_object_name = 'posted_patterns'


#class PatternDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = PostPattern.objects.filter(status=1)
        postpattern = get_object_or_404(queryset, slug=slug)
        postcomment = postpattern.comments.filter(approved=True).order_by("-created_on")

        return render(request, "pattern_detail.html", {
                "postpattern": postpattern,
                "postcomment": postcomment,
            },
        )
