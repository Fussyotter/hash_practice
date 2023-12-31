from django.test import TestCase
from django.urls import reverse
from .models import Url
from django.test import Client
from .utils import base62_encode
from rest_framework.test import APIClient

class UrlShortenerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_index_view_works(self):
        # Send a GET request
        response = self.client.get(reverse('shortener:index'))
        # Assert that the request succeeded
        self.assertEqual(response.status_code, 200)

        # Send a POST request
        response = self.client.post(reverse('shortener:index'), {'long_url': 'https://www.google.com'}, format='json')
        print(response.data)  # Print the response data

        # Print out the response data if the POST request fails
        if response.status_code != 201:
            print(response.data)
        
        # Assert that the request succeeded
        self.assertEqual(response.status_code, 201)

        # Check that the URL was created
        url = Url.objects.get(long_url='https://www.google.com')
        self.assertIsNotNone(url.short_url)
        # Assert that the response contains the short url
        self.assertEqual(response.data['short_url'], url.short_url)

        
class UrlRedirectTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = Url.objects.create(long_url='http://www.example.com', short_url='abc123')

    def test_redirect_view(self):
        app_name = 'shortener'  # Add this line
        response = self.client.get(reverse(f'{app_name}:redirect_view', args=['abc123']))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'http://www.example.com')


class Base62EncodeTestCase(TestCase):
    def test_base62_encode(self):
        num = 123456789
        encoded_value = base62_encode(num)
        print(f'{num} -> {encoded_value}')

        num = 987654321
        encoded_value = base62_encode(num)
        print(f'{num} -> {encoded_value}')


 