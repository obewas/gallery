from django.shortcuts import render
from .models import Image

# Create your views here.
def upload_photo(request):
    image = Image

def show_photo(request):
    display = Image.objects.all()
    return render(request, "photo/index.html",{'Image':display})
