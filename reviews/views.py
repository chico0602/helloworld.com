from django.shortcuts import render
from .models import Review
# Create your views here.


def review_list(request):
    context = {
        'review_list': Review.objects.all().order_by('-created_at'),
    }
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, store_name):
    review = Review.objects.get(store_name=store_name)
    context = {
        'review': review,
    }
    return render(request, 'reviews/review_detail.html', context)
