from django.shortcuts import render

# Create your views here.
from .models import Diary

def top(request):
    context = {
        'diary_list': Diary.objects.all(),
    }
    return render(request, 'diaries/diary_list.html', context)
