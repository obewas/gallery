from django.shortcuts import render
from .models import Image, Comment
from django.views.generic.list import ListView
# Create your views here.
def photo_index(request):
    photos = Image.objects.all()
    context = {"photos": photos}
    return render(request, 'photo/index.html', context)

def photo_details(request, pk):
    snap = Image.objects.get(pk=pk)
    comments = Comment.objects.filter(snap=snap)
    context = {
        'snap': snap, 'comments': comments
    }
    return render(request, 'photo/detail.html', context)

def photo_category(request, category):
    photos = Image.objects.filter(
        categories_name_contains = category
    )
    context = {
        "category": category, 'photos': photos
    }
    return render(request, 'photo/category.html', context)