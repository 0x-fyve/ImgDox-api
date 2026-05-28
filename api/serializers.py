from rest_framework import response
from rest_framework import serializers
from .models import Image, Edit

class Imageserializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ["user"]



class TransformImageserializer(serializers.ModelSerializer):

    class Meta:
        model = Edit
        fields = "__all__"
        read_only_fields = ["user"]        




        

