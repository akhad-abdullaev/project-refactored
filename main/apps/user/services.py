from main.apps.user.repositories import UserRepository
from rest_framework import serializers



class UserService:
    @staticmethod
    def register_user(validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'message': 'Passwords do not match'})
        
        validated_data.pop(confirm_password)
        return UserRepository.create(**validated_data)