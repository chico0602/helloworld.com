from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewCreateForm
# Create your views here.


def review_list(request):
    context = {
        'review_list': Review.objects.all().order_by('-created_at'),
    }
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': get_object_or_404(Review, pk=pk)
    }
    return render(request, 'reviews/review_detail.html', context)

def review_create(request):
    context = {
        'form':ReviewCreateForm()
    }
    return render(request, 'reviews/review_form.html', context)

def review_create_send(request):
    form = ReviewCreateForm(request.POST)
    form.save()
    return redirect('reviews:review_list')
