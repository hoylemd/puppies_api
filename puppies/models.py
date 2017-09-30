from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel


class Puppy(TimeStampedModel):
    owner = models.ForeignKeyField(get_user_model())
