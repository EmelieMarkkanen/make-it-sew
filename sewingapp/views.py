from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from .models import PostPattern
from .models import PostPattern as PP
from django.views.generic import ListView
from .forms import CommentForm, PatternForm


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
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        
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
        else:
            comment_form = CommentForm()

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


class PostPatternForm(LoginRequiredMixin, View):
    form_class = PatternForm
    template_name = 'post_pattern.html'
    login_url = reverse_lazy('login')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            pattern = form.save(commit=False)
            pattern.author = request.user
            pattern.approved = False
            pattern.save()
            messages.success(request, 'Your pattern is awaiting approval from an administrator.')
            return redirect(reverse_lazy('post_pattern'))
        else:
            return render(request, self.template_name, {'form': form})


class EditPattern(View):
    form_class = PatternForm
    template_name = 'edit_pattern.html'

    def get(self, request, slug):
        post = get_object_or_404(PP, slug=slug)
        if request.user != post.author:
            return HttpResponseForbidden()
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, slug):
        post = get_object_or_404(PP, slug=slug)
        if request.user != post.author:
            return HttpResponseForbidden()
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            pattern = form.save(commit=False)
            pattern.author = request.user
            pattern.save()
            messages.success(request, 'Your changes have been saved and sent for review.')
            return redirect('pattern_detail', slug=post.slug)
        else:
            return render(request, self.template_name, {'form': form, 'post': post})


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


class MyPatterns(generic.ListView):

    model = PostPattern
    template_name = 'my_patterns.html'

    def get(self, request):

        queryset = PP.objects.filter(
            author=request.user.id).order_by('-created_on')
        queryset_dict = {
            'my_patterns': queryset
        }

        return render(
            request,
            self.template_name,
            queryset_dict
        )


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