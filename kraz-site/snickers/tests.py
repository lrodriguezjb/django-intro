from django.test import SimpleTestCase
from django.urls import reverse

class snickers_test(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_templates(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base_layout.html')

    def test_about_templates(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base_layout.html')

