from main.apps.category.repositories import CategoryRepository
from django.core.exceptions import ObjectDoesNotExist


class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    def list_categories(self):
        return self.repo.get_all()
    
    def retrieve_category(self, category_id):
        return self.repo.get_by_id(category_id)
    
    def create_category(self, validated_data):
        return self.repo.create(**validated_data)
    
    def update_category(self, product_id, validated_data):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ObjectDoesNotExist("Product not found")
        return self.repo.update(product, **validated_data)

    def delete_category(self, product_id):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ObjectDoesNotExist("Product not found")
        self.repo.delete(product)
        return True
