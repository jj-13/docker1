from faker import Faker
from productos.models import Product

faker = Faker()


class ProductFactory:

    def build_product_json(self):
        return {
            'name': faker.name(),
            'description': faker.text()
        }

    def create_product(self):
        return Product.objects.create(**self.build_product_json())
