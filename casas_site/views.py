from django.shortcuts import render
from django.views import View
from .text import context
from .forms import ContactForm

class IndexView(View):

    def get(self, request):
        return render(request, 'casas_site/index.html', context)


class ContactView(View):

    def get(self, request):
        context['form'] = ContactForm()
        return render(request, 'casas_site/contact.html', context)


class AboutUsView(View):

    def get(self, request):
        return render(request, 'casas_site/about.html', context)