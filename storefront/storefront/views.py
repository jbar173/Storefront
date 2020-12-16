from django.shortcuts import render
from django.views.generic import TemplateView


## STOREFRONT VIEWS:

class HomePage(TemplateView):
    template_name = 'home.html'

class LoggedInPage(TemplateView):
    template_name = 'logged_in.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class AboutPage(TemplateView):
    template_name = 'about.html'
