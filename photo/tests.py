from django.test import TestCase
from .models import Image
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.
class ImageTestCase(TestCase):
    def test_save_image(self):
        newImage = Image()
        newImage.image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')