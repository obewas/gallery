from django.db import models


# Create your models here.
class Location(models.Model):
    geo_tag = models.CharField(max_length=30)
    season = models.CharField(max_length=30)

class Category(models.Model):
    cat = models.CharField(max_length=30)

    def __str__(self):
        return self.cat

class Image(models.Model):
    image = models.CharField(max_length=50)
    image_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date_of_upload = models.DateField(max_length=50, auto_now=True)
    photo_upload = models.ImageField(upload_to='media/', null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save_image(self):
        newImage = Image()
        newImage.image = models.ImageField(upload_to='media/', blank=True)
        newImage.save()

    def delete_image(self):
        pass
    def update_image(self):
        pass
    def get_image_by_id(self, id):
        pass
    def search_image_category(self, category):
        pass
    def filter_by_location(self,location):
        pass






