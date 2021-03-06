from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions

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
    def create(self, validated_data):
        return Puppy.objects.create(
            file=validated_data['file'],
            title=validated_data['title'],
            body=validated_data['body'],
            owner=self.context['request'].user,
        )

    def validate(self, data):
        if self.context['request'].user != self.instance.owner:
            raise exceptions.PermissionDenied(
                "Cannot edit posts owned by another user.",
            )

        return data

    class Meta:
        model = Puppy
        fields = (
            'url',
            'owner',
            'title',
            'body',
            'file',
            'created',
            'modified',
        )
        read_only_fields = ('owner', 'created', 'modified')
