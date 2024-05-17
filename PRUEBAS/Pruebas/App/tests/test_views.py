from django.test import TestCase
from django.urls import reverse
from App.models import Post  # Importa el modelo para pruebas adicionales

class TestViews(TestCase):
    
    def test_create_post_view(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_create_post_submission(self):
        response = self.client.post(reverse('create_post'), {'title': 'New Title', 'content': 'New Content'})
        self.assertEqual(response.status_code, 302)  # Asegúrate de que redirige después de crear
        self.assertEqual(Post.objects.last().title, 'New Title')

    def test_delete_post_view(self):
        post = Post.objects.create(title='Test Title', content='Test Content')
        response = self.client.post(reverse('delete_post', args=[post.id]))
        self.assertEqual(response.status_code, 302)  # Asegúrate de que redirige después de eliminar
        self.assertEqual(Post.objects.count(), 0)
