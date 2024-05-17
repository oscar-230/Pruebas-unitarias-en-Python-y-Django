from django.test import TestCase
from App.models import Post

class TestModels(TestCase):

    def test_post_creation(self):
        post = Post.objects.create(title='Test Title', content='Test Content')
        self.assertEqual(post.title, 'Test Title')
        self.assertEqual(post.content, 'Test Content')
