from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Puppy


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = (
            'url',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        )


class PuppySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Puppy
        fields = (
            'url',
            'file',
            'title',
            'body',
            'owner',
            'created',
            'modified',
        )
        read_only_fields = ('owner', 'created', 'modified')

    def create(self, validated_data):
        return Puppy.objects.create(
            file=validated_data['file'],
            title=validated_data['title'],
            body=validated_data['body'],
            owner=self.context['request'].user,
        )
