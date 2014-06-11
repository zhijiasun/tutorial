from rest_framework import serializers
from django.contrib.auth.models import User
from polls.models import Poll
from rest.models import Album,Track

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
