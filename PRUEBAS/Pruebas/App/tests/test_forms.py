from django.test import TestCase
from App.forms import PostForm

class TestForms(TestCase):

    def test_post_form_valid_data(self):
        form = PostForm(data={'title': 'Test Title', 'content': 'Test Content'})
        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
