from django.contrib import admin
from .models import Image, Category, Location
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'category', 'location', 'created']
    ordering = ['-created']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['geo_tag']
    ordering = ['geo_tag']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat']
    ordering = ['cat']

admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
