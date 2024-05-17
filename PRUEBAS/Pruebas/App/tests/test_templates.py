from django.test import TestCase

class TestTemplates(TestCase):

    def test_create_post_template(self):
        response = self.client.get('/App/create/')
        self.assertTemplateUsed(response, 'create_post.html')

    def test_post_list_template(self):
        response = self.client.get('/App/list/')
        self.assertTemplateUsed(response, 'post_list.html')
