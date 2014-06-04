from django.shortcuts import render
from django.views.generic import TemplateView,View,RedirectView
from cbv.forms import ContactForm
from django.views.generic.edit import FormView

# Create your views here.

class TestTemplateView(TemplateView):
    """
    """

    template_name = 'testtemplate.html'


class TestView(View):
    pass


class TestRedirectView(RedirectView):
    url = '/cbv/testtemplateview/'


class ContactView(FormView):
    template_name = 'testform.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self):
        pass
