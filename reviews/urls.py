from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewList.as_view(), name='review_list'),
    path('detail/<str:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('create/', views.ReviewCreate.as_view(), name='review_create'),
    path('update/<str:pk>/', views.ReviewUpdate.as_view(), name='review_update'),
    path('delete/<str:pk>/', views.ReviewDelete.as_view(), name='review_delete'),
]
