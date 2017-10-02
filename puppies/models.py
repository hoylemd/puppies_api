from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel


def user_directory_path(instance, filename):
    return 'users/{}/{}'.format(instance.owner.username, filename)


class Puppy(TimeStampedModel):
    owner = models.ForeignKey(get_user_model())
    file = models.FileField(upload_to=user_directory_path)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
