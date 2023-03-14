from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
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
        if post.likes.filter(id=request.user.id).exists():
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
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        if 'postpattern_id' in request.POST:
            post.number_of_likes += 1
            post.likes.add(request.user)
            post.save()
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


class EditPattern(LoginRequiredMixin, View):
    form_class = PatternForm
    template_name = 'edit_pattern.html'

    def get(self, request, slug):
        post = get_object_or_404(PP, slug=slug, author=request.user)
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, slug):
        post = get_object_or_404(PP, slug=slug, author=request.user)
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            pattern = form.save(commit=False)
            pattern.author = request.user
            pattern.status = 0
            pattern.save()
            messages.success(request, 'Your changes have been saved and sent for review. Pattern will be available after approval.')
            return redirect('my_patterns')
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
    paginate_by = 6

    def get(self, request):
        post_patterns = PP.objects.filter(author=request.user.id).order_by('-created_on').filter(status=1)
        paginator = Paginator(post_patterns, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'my_patterns': page_obj}
        return render(request, self.template_name, context)
        

class PatternLike(View):

    def post(self, request, slug):
        """
        Post method for liking and unliking a pattern.
        """
        pattern = get_object_or_404(PP, slug=slug)

        if pattern.likes.filter(id=request.user.id).exists():
            pattern.likes.remove(request.user)
        else:
            pattern.likes.add(request.user)
            messages.success(request, 'Pattern was saved to your liked patterns!')

        return HttpResponseRedirect(reverse_lazy('pattern_detail', args=[slug]))


class LikedPatterns(generic.ListView):
    paginate_by = 6
    
    def get(self, request, *args, **kwargs):
        """
        Get method to render template and return queryset objects.
        """
        user = request.user
        liked_patterns = PP.objects.filter(likes=user).filter(status=1)
        paginator = Paginator(liked_patterns, self.paginate_by)
        page = request.GET.get('page')
        liked_patterns = paginator.get_page(page)
        context = {'liked_patterns': liked_patterns, 'page_obj': liked_patterns}

        return render(request, 'liked_patterns.html', context)


class DeletePattern(LoginRequiredMixin, DeleteView):
    model = PostPattern
    success_url = reverse_lazy('my_patterns')

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(PP, slug=slug, author=request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Pattern was successfully deleted')
        return super().delete(request, *args, **kwargs)