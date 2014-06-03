from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    newsletter_subscribe = models.BooleanField(default=False)

    class Meta:
        app_label = 'rest'

settings.REST_PROFILE_MODULE = UserProfile
