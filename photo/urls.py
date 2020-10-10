from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'',views.photo_index, name='viewPhotos'),
    url(r'<int:pk>/', views.photo_details, name='photo_details'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)