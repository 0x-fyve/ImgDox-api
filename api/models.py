from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    added_at = models.DateTimeField(auto_now_add=True)

class Edit(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    height = models.IntegerField()
    width = models.IntegerField()
    grayscale = models.BooleanField(default=False)
    sepolia = models.BooleanField(default=False)
    updated_at = models.DateTimeField( auto_now=False, auto_now_add=False)
    