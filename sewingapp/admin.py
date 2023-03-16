from django.contrib import admin
from .models import PostPattern, PostComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PostPattern)
class PostAdmin(SummernoteModelAdmin):
    """
    Class for the Pattern section of the admin area.
    Organises the display of posts, filtering and searchbar.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class for the Comment section of the admin area.
    Organises the display of comments, filtering and searchbar.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
