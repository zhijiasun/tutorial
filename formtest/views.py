from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest
from forms import Contact

# Create your views here.


def contact(request):
	if request.method == "POST":
		print 'aaaaaaaaaa'
		myform = Contact(request.POST)
		if myform.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		myform = Contact()
	return render(request,'form.html',{'form':myform,})
