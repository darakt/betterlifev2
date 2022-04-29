from rest_framework import serializers
from .models import User
from comments.serializers import CommentSerializer

class UserSerializer(serializers.ModelSerializer):
    has_written = CommentSerializer(many= True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'has_written']
