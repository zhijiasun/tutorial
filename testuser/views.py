from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def testuser_index(request):
	if request.method == 'POST':
		print request.POST['username']	
		print request.POST['password']
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			print user.username
			login(request,user)
			return render_to_response('index.html',context_instance=RequestContext(request))
		else:
			return render_to_response('index.html',context_instance=RequestContext(request))

	else:
		print request.method
		print request.user.username
		#logout(request)
		return render_to_response('index.html',context_instance=RequestContext(request))

def testuser_login(request):
	print request.POST['username']
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username, password)
	if not user:
		return HttpResponseRedirect('/testuser/index/')
	else:
		login(request,user)


def testuser_register(request):
	pass

