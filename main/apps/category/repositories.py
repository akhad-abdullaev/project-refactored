from test_proj.main.apps.category.models import Category



class CategoryRepository:
    @staticmethod
    def get_all():
        return Category.objects.all()
    

    @staticmethod
    def get_by_id(category_id):
        return Category.objects.filter(id=category_id).first()
    

    @staticmethod
    def create(**data):
        return Category.objects.create(**data)
    

    @staticmethod
    def update(instance, **data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    

    @staticmethod
    def delete(instance):
        return instance.delete()