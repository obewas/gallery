from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    geo_tag = models.CharField(max_length=30)
    season = models.CharField(max_length=30)

    def __str__(self):
        return self.geo_tag, self.season

class Category(models.Model):
    cat = models.CharField(max_length=30)

    def __str__(self):
        return self.cat

class Image(models.Model):
    image = models.ImageField(upload_to='media/', null=True)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(max_length=50, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def save_image(cls):
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


class Comment(models.Model):
    post = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(max_length=50, auto_now_add=True)
    modified = models.DateTimeField(max_length=50, auto_now=True)




