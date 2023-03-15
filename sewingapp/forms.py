from .models import PostComment, PostPattern, SUGGESTED_FABRICS
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
    PatternForm class. Sets the model and fields for the pattern form.
    Also assigns widget to suggested fabrics for styling purposes.
    """
    suggested_fabrics = forms.MultipleChoiceField(choices=SUGGESTED_FABRICS, widget=forms.CheckboxSelectMultiple(attrs={'class': 'fabric-list'}))
    
    class Meta:
        model = PostPattern
        fields = (
            'title',
            'description',
            'file',
            'featured_image',
            'difficulty',
            'suggested_fabrics',
        )