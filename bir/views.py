from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'