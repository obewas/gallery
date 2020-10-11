from django.shortcuts import render
from .models import Image, Category, Location


# Create your views here.
def index(request):
    """View function for home page of site."""
    photos = Image.objects.all().order_by('-created')
    no_of_photos = Image.objects.all().count()
    cat = Category.objects.all()
    context = {"photos": photos, 'no_of_photos': no_of_photos, 'cat': cat}
    return render(request, 'photo/index.html', context=context)

def photo_details(request, pk):
    snap = Image.objects.get(pk=pk)
    context = {
        'snap': snap
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


