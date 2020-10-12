from django.db import models
from django.contrib.auth.models import User
from djchoices import ChoiceItem, DjangoChoices
# Create your models here.
class Location(models.Model):
    geo_tag = models.CharField(max_length=30, unique=True)
    class Meta:
        ordering = ['geo_tag']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.geo_tag

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()



class Category(models.Model):
    cat = models.CharField(max_length=30, null=True)

    class Meta:
        ordering = ["cat"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    #def __str__(self):
    #    return self.cat


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, related_name='category',on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["created"]
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def summary(self):
        return self.description[:100] + " ......"

    def pub_date_pretty(self):
        return self.created.strftime('%b %e %Y')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        pass

    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images

    def search_image(category):
        pass

    def filter_by_location(location):
        pass

    @classmethod
    def search_by_category(cls, search_term):
        searched_images = cls.objects.filter(category__icontains=search_term)
        return searched_images







