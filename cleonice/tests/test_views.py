from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
    
    def tearDown(self):
        pass

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    