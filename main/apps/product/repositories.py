from test_proj.main.apps.product.models import Product



class ProductRepository:
    @staticmethod
    def get_all():
        return Product.objects.select_related('category').all()
    

    @staticmethod
    def get_by_id(product_id):
        return Product.objects.filter(id=product_id).first()
    

    @staticmethod
    def create(**data):
        return Product.objects.create(**data)
    

    @staticmethod
    def update(instance, **data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    

    @staticmethod
    def delete(instance):
        return instance.delete()