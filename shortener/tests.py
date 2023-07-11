from django.test import TestCase
from django.urls import reverse
from .models import Url
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
    
