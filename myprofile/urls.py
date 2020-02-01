from django.urls import path
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('resume/', views.Resume.as_view(), name='resume'),
]
