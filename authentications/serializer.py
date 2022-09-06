from rest_framework import serializers
from app.serializer import *
from .models import User
# User Serializer

# List 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = User
        fields = "__all__"

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'is_superuser', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'], is_superuser=validated_data['is_superuser'],
                                        is_active=True)
        return user

   

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('date_created', 'date_modified')