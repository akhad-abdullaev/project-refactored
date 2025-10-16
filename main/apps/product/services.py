from test_proj.main.apps.product.repositories import ProductRepository



class ProductService:
    @staticmethod
    def list_product():
        return ProductRepository.get_all()
    

    @staticmethod
    def retrieve_product(product_id):
        return ProductRepository.get_by_id(product_id)
    

    @staticmethod
    def create_product(validated_data):
        return ProductRepository.create(**validated_data)
    

    @staticmethod
    def update_product(product, validated_data):
        return ProductRepository.update(product, **validated_data)
    
    
    @staticmethod
    def delete_product(product):
        return ProductRepository.delete(product)