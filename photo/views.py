from django.shortcuts import render
import os
from django.conf import settings
from django.templatetags.static import static
# Create your views here.
def show_photo(request):
    path = settings.MEDIA_ROOT
    img_lst = os.listdir(path + '/images')
    context = {'images' : img_lst}
    return render(request, "photo/index.html", context)
