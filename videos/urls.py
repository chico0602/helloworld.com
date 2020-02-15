from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.VideoList.as_view(), name='video_list'),
]
