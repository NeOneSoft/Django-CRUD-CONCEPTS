from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TokenTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')

    def test_authenticate(self):
        result = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})

        assert 'access' in result.data

    def test_valid_token(self):
        result = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})
        token = result.data['access']

        libros_result = self.client.get('/api/v1/libros/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))

        assert libros_result.status_code == 200
