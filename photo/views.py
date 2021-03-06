from django.shortcuts import render
from .models import Image, Category, Location
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    """View function for home page of site."""
    photos = Image.objects.all().order_by('-created')
    no_of_photos = Image.objects.all().count()
    context = {"photos": photos, 'no_of_photos': no_of_photos}
    return render(request, 'photo/index.html', context=context)

def single_photo_details(request, image_id):
    """return details of single photo"""
    photo_detail = get_object_or_404(Image, pk=image_id)
    context = {'photo_detail': photo_detail}
    return render(request, 'photo/detail.html', context)

def photo_category(request, cat):

    photos = Image.objects.filter(
     categories_name_contains = cat
    )
    context = {
       "cat": cat, 'photos': photos
   }
    return render(request, 'photo/category.html', context)

def photo(request, pk):
    try:
        image = Image.objects.get(id=pk)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'photo/image.html', {'image':image})


def about_us(request):
    '''
    Function that returns information about the website
    '''
    return render(request, 'photo/about.html')

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photo/search.html', {"message": message, "images": searched_images})
    else:
        message = "You have not searched for any category"

        return render(request, 'photo/search.html', {"message": message})
def gallery(request):
    '''
    gallery function returns the list of photos in the database
    '''
    gallery = Image.objects.all()
    return render(request, 'photo/gallery.html', {'gallery':gallery})

def sports(request):
    sports_category = Category.objects.get(pk=1)
    sports = Image.objects.all().filter(category=sports_category)
    return render(request, 'category/sports.html', {'sports': sports})


def family(request):
    family_category = Category.objects.get(pk=2)
    family = Image.objects.filter(category=family_category)
    return render(request, 'category/family.html', {'family': family})


def travel(request):
    travel_category = Category.objects.get(pk=3)
    travel = Image.objects.filter(category=travel_category)
    return render(request, 'category/travel.html', {'travel': travel})


def technology(request):
    tech_category = Category.objects.get(pk=4)
    tech = Image.objects.filter(category=tech_category)
    return render(request, 'category/technology.html', {'tech': tech})