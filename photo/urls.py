from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'', views.index, name='index'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)