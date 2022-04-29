from pyexpat import model
from rest_framework import serializers
from .models import Project
from organizations.serializers import OrganizationSerializer
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class ProjectSerializer(serializers.Serializer):
    organization = OrganizationSerializer(many=False)
    owner = UserSerializer(many=False)
    members = UserSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Project
        fields = [ 'title', 'description', 'goal']