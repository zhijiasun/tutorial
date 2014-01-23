from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.

def snippet_index(request):
	return	render_to_response('index.html')


class JSONResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse,self).__init__(content,**kwargs)


@csrf_exempt
def snippet_list2(request):
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets,many=True)
		return JSONResponse(serializer.data)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data,status=201)
		else:
			return JSONResponse(serializer.error,status=400)


"""
@csrf_exempt
def snippet_detail(request,pk):
	print '!!!!'
	try:
		snippet = Snippet.objects.get(pk=pk)
	except:
		return HttpResponse(status=404)

	print '~~~~~'
	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		print 'the pk is ' + pk
		data = JSONParser().parse(request)
		print 'dfdsafds'
		serializer = SnippetSerializer(snippet,data = data)
		if serializer.is_valid():
			print 'aaaaa'
			serializer.save()
			return HttpResponse(serializer.data)
		else:
			print 'bbb'
			return JSONResponse(serializer.errors,status=400)

	elif request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)

"""

"""
refactor the views.py
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET','POST'])
def snippet_list(request):
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets,many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk):
	pass