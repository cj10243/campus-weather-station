from django.test import TestCase

# Create your tests here.
class HomeViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

class StatusViewTests(TestCase):
    def test_status_view(self):
        response = self.client.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/status.html')

class AboutViewTests(TestCase):
    def test_about_view(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')