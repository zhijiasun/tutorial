from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	return HttpResponse('Hello World!')


def detail(request):
	pass
	
def results(request):
	pass

def vote(request):
	pass