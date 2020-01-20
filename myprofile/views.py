from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def top(request):
    context = {
        'name': 'ちこ',
    }
    return render(request, 'myprofile/top.html', context)

def resume(request):
    return render(request, 'myprofile/resume.html')
