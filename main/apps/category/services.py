from test_proj.main.apps.category.repositories import CategoryRepository



class CategoryService:
    @staticmethod
    def list_categories():
        return CategoryRepository.get_all()
    
    @staticmethod
    def retrieve_category(category_id):
        return CategoryRepository.get_by_id(category_id)
    
    @staticmethod
    def create_category(validated_data):
        return CategoryRepository.create(**validated_data)
    
    @staticmethod
    def update_category(category, validated_data):
        return CategoryRepository.update(category, **validated_data)
    
    @staticmethod
    def delete_category(category):
        return CategoryRepository.delete(category)
