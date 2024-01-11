from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from productos.models import Product
from test.factories.api_productos.product_factories import ProductFactory
import pdb


class ProductTestCase(APITestCase):

    def test_create_product(self):
        producto = ProductFactory().build_product_json()

        response = self.client.post(
            #'http://localhost:8000/api/products/',
            'http://ip172-18-0-21-cmg47pks9otg00a8q91g-8000.direct.labs.play-with-docker.com/api/products/',
            producto,
            format='json'
        )
        #pdb.set_trace()
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Product.objects.all().count(), 1)
        self.assertEquals(response.data['message'], 'Producto creado')
        self.assertEquals(Product.objects.get(id=1).name, producto['name'])

    def test_get_detail_product(self):
        producto = ProductFactory().create_product()

        response = self.client.get(
            #f'http://localhost:8000/api/products/{producto.id}/'
            f'http://ip172-18-0-21-cmg47pks9otg00a8q91g-8000.direct.labs.play-with-docker.com/api/products/{producto.id}/'
        )
        #pdb.set_trace()
        self.assertEquals(response.data['id'], producto.id)
    def test_get_all_products(self):
        producto = ProductFactory().create_product()

        response = self.client.get(
            #'http://localhost:8000/api/products/'
            'http://ip172-18-0-21-cmg47pks9otg00a8q91g-8000.direct.labs.play-with-docker.com/api/products/'
        )
        #pdb.set_trace()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data[0]['name'], producto.name)


