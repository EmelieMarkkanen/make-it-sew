from .models import PostComment, PostPattern
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body',)


class PatternForm(forms.ModelForm):
    class Meta:
        model = PostPattern

        widgets = {
            'description': SummernoteWidget(),
        }

        fields = (
            'title',
            'file',
            'featured_image',
            'description',
            'difficulty',
            'suggested_fabrics',
        )