from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator
from django.contrib import messages
from .models import PostPattern
from .models import PostPattern as PP
from django.views.generic import ListView
from .forms import CommentForm


class PostPattern(generic.ListView):
    model = PostPattern
    queryset = PostPattern.objects.filter(status=1, featured_pattern=True).order_by("-created_on")
    template_name = "index.html"
    context_object_name = 'posted_patterns'


class PatternDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = PP.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        page = 'pattern_detail'
        approved = False
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "pattern_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "page": page,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = PP.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        page = 'pattern_detail'
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False) 
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, "Your comment has been submitted and is pending approval.")
        else:
            comment_form = CommentForm()
            messages.error(request, "There was an error submitting your comment.")

        return render(
            request,
            "pattern_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "page": page,
                "liked": liked,
                "comment_form": CommentForm(),
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


class LikedPatterns(generic.ListView):

    model = PostPattern
    queryset = PP.objects.filter(status=1).order_by('-created_on')
    template_name = "liked_patterns.html"
    paginate_by = 6
    context_object_name = 'posted_patterns'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'liked_patterns'
        return context