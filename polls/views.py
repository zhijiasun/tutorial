from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
    print reverse('index')
    return HttpResponse('Hello World!')


def detail(request):
	pass
	
def results(request):
	pass

def vote(request):
	pass
