from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from serializers import *
from django.views.decorators.csrf import csrf_exempt
from polls.models import Poll
import pdb
from rest.models import Album,Track

# Create your views here.
@api_view(['GET'])
def album_list(request):
    print 'aaaaa'
    if request.method == 'GET':
        print 'bbbb'
    albums = Album.objects.all()
    print albums
    aserializer = AlbumSerializer(albums,many=True)
    print aserializer.data
    return Response(aserializer.data)

@csrf_exempt
@api_view(['POST'])
def register_user(request):
    print 'aaaa'
    print request.method
    print request.DATA
    print 'ddd'
    user = UserSerializer(data=request.DATA)
    if user.is_valid():
        print 'valid'
        pdb.set_trace()
        u = User.objects.create_user(username=user.init_data['username'],email=user.init_data['email'],password=user.init_data['password'])
        u.save()
        return Response(user.data,status = status.HTTP_201_CREATED)
    else:
        pdb.set_trace()
        return Response(uesr.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def operate_poll(request):
    print 'aaaabbb'
    if request.method == 'GET':
        polls = Poll.objects.all()
        pserializered = PollSerializer(polls,many=True)
        return Response(pserializered.data)
    if request.method == 'POST':
        print 'method is:%s'%request.method
        print request.DATA
        p = PollSerializer(data=request.DATA)
        if p.is_valid():
            p.save()
            return Response(p.data,status=status.HTTP_201_CREATED)
        else:
            return Response(p.errors,status = status.HTTP_400_BAD_REQUEST)

