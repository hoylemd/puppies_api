from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Puppy


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'email', 'is_staff')


class PuppySerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Puppy
