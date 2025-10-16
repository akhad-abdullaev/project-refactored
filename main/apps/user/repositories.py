from django.contrib.auth.models import User



class UserRepository:
    @staticmethod
    def create(**data):
        return User.objects.create(**data)
    
    
    @staticmethod
    def get_by_username(username):
        return User.objects.filter(username=username)