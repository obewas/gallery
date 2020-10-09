from django.shortcuts import render
from .models import Image

# Create your views here.
#function that serves the welcome page
def index(request):

    # get all current photo by the latest
    all_photos = Image.objects.all().order_by('-id')
    return render(request, 'photo/index.html', {'all_photos':all_photos})
def upload_photo(request):
    image = Image

def show_photo(request):
    display = Image.objects.all()
    return render(request, 'photo/index.html',{'Image':display})
