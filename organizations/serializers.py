from rest_framework import serializers
from .models import Organization
from users.serializers import UserSerializer

class OrganizationSerializer(serializers.Serializer):
    members = UserSerializer(many=True)
    admins = UserSerializer(many=True)

    class Meta:
        model = Organization
        fields = [ 'name', 'description', 'language']