from django import forms

class Contact(forms.Form):
	subject = forms.CharField()
	message = forms.CharField(max_length=100)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)