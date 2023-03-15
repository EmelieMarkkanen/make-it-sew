from django.test import TestCase
from .forms import CommentForm, PatternForm
from django.core.files.uploadedfile import SimpleUploadedFile


class TestCommentForm(TestCase):
    def test_valid_form(self):
        """
        Test that the form is valid when a valid body is provided
        """
        data = {'body': 'This is a valid comment'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Test that the form is invalid when body is not provided
        """
        data = {'body': ''}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
