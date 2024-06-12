from django.urls import reverse
from django.test import TestCase, Client
from .models import CSVFile
from .forms import CSVFileForm
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_index_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsInstance(response.context['form'], CSVFileForm)

    def test_index_post_valid(self):
        with open('path/to/valid/csv.csv', 'rb') as file:
            data = {'csv_file': file}
            response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('graph_path' in response.context)

    def test_index_post_invalid(self):
        response = self.client.post(self.url, {'csv_file': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFalse('graph_path' in response.context)

class MarketNewsViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('market_news_view')

    def test_market_news_get(self):
        response = self.client.get(self.url, {'category': 'general', 'minId': '10'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), MarketNews.objects.count())

    def test_market_news_invalid_category(self):
        response = self.client.get(self.url, {'category': 'invalid_category'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
