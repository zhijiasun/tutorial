from django.shortcuts import render
from django.views.generic import TemplateView,View,RedirectView
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView,FormView
from cbv.forms import ContactForm
from cbv.models import Article

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


class TestListView(ListView):
    model = Article
    template_name = 'testlistview.html'

    def get_context_data(self):
        pass
