from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Location(models.Model):
    geo_tag = models.CharField(max_length=30)
    def __str__(self):
        return self.geo_tag

class Category(models.Model):
    cat = models.CharField(max_length=30)

    def __str__(self):
        return self.cat


class Image(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField('Category', related_name='photos')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    @classmethod
    def save_image(cls, ):
        #create a new photo record in gallery
        new_image = Image()
        new_image.save()

    def delete_image(self):
        snap = Image.objects.get(pk=1)
        if snap.image:
            if os.path.isfile(snap.image.path):
                os.remove(snap.image.path)
    def update_image(self, request):
        modify = Image.objects.get(pk=1)
        modify.image = Image()
        modify.save()
    def get_image_by_id(self, id):
        all_images = Image.objects.all(id)
        image_by_id = Image.objects.filter(id=1)
        return image_by_id


    def search_image_category(self, category):
        cat = Image.objects.filter(category)

        pass
    def filter_by_location(self,location):
        pass






