from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.CharField(max_length=50)
    image_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date_of_upload = models.DateField(max_length=50, null=True)
    photo_upload = models.ImageField(upload_to='media/', null=True)
