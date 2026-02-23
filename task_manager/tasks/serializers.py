from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model - used for registration and basic user info.
    Password is write-only (never returned in responses).
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}   # important: hides password in responses
        }

    def create(self, validated_data):
        """
        Create and return a new user, hashing the password correctly.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    Owner is read-only (automatically set to request.user).
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'completed',
            'created_at',
            'updated_at',
            'owner'
        ]
        read_only_fields = ['created_at', 'updated_at', 'owner']