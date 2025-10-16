from main.apps.product.repositories import ProductRepository
from django.core.exceptions import ObjectDoesNotExist


class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    def list_product(self):
        return self.repo.get_all()
    

    def retrieve_product(self, product_id):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ObjectDoesNotExist("Product not found")
        return product
    

    def create_product(self, validated_data):
        return self.repo.create(**validated_data)
    

    def update_product(self, product_id, validated_data):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ObjectDoesNotExist("Product not found")
        return self.repo.update(product, **validated_data)

    def delete_product(self, product_id):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ObjectDoesNotExist("Product not found")
        self.repo.delete(product)
        return True