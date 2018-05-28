from django.test import TestCase, Client, RequestFactory
from pessoas.models import Pessoa
from mock import patch
import json

# Create your tests here.
class PessoaViewTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = Pessoa.objects.create(id=1, name='jacob', gender='M', age=25)

    def test_get_return_http_200(self):
        response = self.client.get('/pessoas/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_post_return_http_201(self):
        response = self.client.post('/pessoas/', {
                                                    "name":"Paulo",
                                                    "gender":"M",
                                                    "age":25,
                                                }, format = 'json')
        self.assertEqual(response.status_code, 201)                                                

    def test_get_with_id_returns_http_200(self):
        response = self.client.get('/pessoas/1/', format='json')
        self.assertEqual(response.data, {'id':1, 'name':'jacob', 'gender':'M', 'age':25})        
        self.assertEqual(response.status_code, 200)

    def test_can_delete_pessoa(self):
        response = self.client.delete('/pessoas/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Pessoa.objects.count(), 0)

    def test_can_change_pessoa(self):
        pessoa = { "id": 1, "name": "Paulo", "gender": "M", "age": 15 }
        response = self.client.put('/pessoas/1/', '{"id":1, "name":"Paulo", "gender":"M", "age": 15}', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, pessoa)