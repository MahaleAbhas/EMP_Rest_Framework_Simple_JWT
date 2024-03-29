from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')