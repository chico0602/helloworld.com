from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.http import HttpResponse
from django.template import loader


class Top(generic.TemplateView):
    template_name = 'myprofile/top.html'
    extra_context = {'name': 'ちこ'}

class Resume(generic.TemplateView):
    template_name = 'myprofile/resume.html'
