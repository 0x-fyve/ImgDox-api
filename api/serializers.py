from rest_framework import response
from rest_framework import serializers
from .models import Image

class Imageserializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ["user"]



        

