from rest_framework import viewsets
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        print(request)
        user = User.objects.create(request)
        print(user.toJson())
        return Response(user)
