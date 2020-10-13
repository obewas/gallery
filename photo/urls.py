from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$',views.index, name='photo/index'),
    url(r'<int:pk>/', views.single_photo_details, name='photo/single_photo_details'),
    url(r'<category>/', views.photo_category, name='photo/photo_category'),
    url(r'<image>/(\d+)', views.photo, name='photo/image'),
    url(r'^gallery/$', views.gallery, name='photo/gallery'),
    url(r'^about/$', views.about_us, name = 'photo/about_us'),
    url(r'^search/', views.search_category, name = 'photo/search_category'),
    url(r'^category/sports/$', views.sports, name = 'sports'),
    url(r'^category/technology/$', views.technology, name = 'technology'),
    url(r'^category/family/$', views.family, name = 'family'),
    url(r'^category/travel/$', views.travel, name = 'travel'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)