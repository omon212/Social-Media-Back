from rest_framework import serializers
from .models import *


class UserRegisterSRL(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class UserLoginSRL(serializers.Serializer):
    username = serializers.CharField(max_length=16)
    password = serializers.CharField(max_length=36)
