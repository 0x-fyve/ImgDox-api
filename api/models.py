from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} image"

class Edit(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    height = models.IntegerField()
    width = models.IntegerField()
    grayscale = models.BooleanField(default=False)
    sepolia = models.BooleanField(default=False)
    updated_at = models.DateTimeField( auto_now=False, auto_now_add=False)
    