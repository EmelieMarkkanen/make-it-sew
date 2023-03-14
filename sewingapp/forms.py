from .models import PostComment, PostPattern
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    Comment Form Class.
    Sets the model and fields for the comment form.
    """
    class Meta:
        model = PostComment
        fields = ('body',)


class PatternForm(forms.ModelForm):
    """
    PatternForm class. Sets the model and fields for the recipe form.
    Also assigns summernote widget to description form field.
    """
    class Meta:
        model = PostPattern

        #Summernote widget
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