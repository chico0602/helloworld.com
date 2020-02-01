from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Diary

class Top(generic.ListView):
    queryset = Diary.objects.all()
    ordering = 'created_at'
