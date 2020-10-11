from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'',views.index, name='photo/index'),
    url(r'<int:pk>/', views.photo_details, name='photo_details'),
    url(r'<category>/', views.photo_category, name='photo_category'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)