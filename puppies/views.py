from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import UserSerializer, PuppySerializer
from .models import Puppy


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class PuppyViewSet(viewsets.ModelViewSet):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer


class FeedView(ListAPIView):
    serializer_class = PuppySerializer

    def get_queryset(self):
        user = get_user_model().objects.get(username=self.kwargs['username'])
        return user.puppy_set.order_by('-created')


class CreateUserView(CreateAPIView):
    """Special view to allow anonymous users to register"""
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer
