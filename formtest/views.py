from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest
from forms import Contact

# Create your views here.


def contact(request):
	if request.method == "POST":
		form = Contact(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = Contact()
	print 'aaaa'
	return render(request,'index.html',{'form':form,})