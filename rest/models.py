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

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)


class Track(models.Model):
    album = models.ForeignKey(Album,related_name='tracks')#default realted_name is track_set
    order = models.IntegerField()
    title = models.CharField(max_length = 100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album','order')

    def __unicode__(self):
        return '%s:%s' % (self.order,self.title)
