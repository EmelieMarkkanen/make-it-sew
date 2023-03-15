from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    def test_valid_form(self):
        data = {'body': 'This is a valid comment'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'body': ''}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())