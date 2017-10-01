from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CreateUserView(CreateAPIView):
    """Special view to allow anonymous users to register"""
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer
