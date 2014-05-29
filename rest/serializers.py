from rest_framework import serializers
from django.contrib.auth.models import User
from polls.models import Poll

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
