from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest
from forms import *

# Create your views here.
def example(request):
    exampleform = ExampleForm()
    return render(request,'exampleform.html',{'exampleform':exampleform,})



def contact(request):
	if request.method == "POST":
		myform = Contact(request.POST)
		if myform.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		myform = Contact()
	return render(request,'form.html',{'form':myform,})
