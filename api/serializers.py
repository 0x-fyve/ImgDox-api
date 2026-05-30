from rest_framework import response
from rest_framework import serializers
from .models import Image, Edit

class Imageserializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ["user"]

class Resizeserializer(serializers.Serializer):
    width = serializers.IntegerField()
    height = serializers.IntegerField()

class Rotateserializer(serializers.Serializer):
    angle= serializers.IntegerField()

class FormatSerializer(serializers.Serializer):

    format = serializers.ChoiceField(
        choices=["JPEG", "PNG", "WEBP"]
    )

class CropSerializer(serializers.Serializer):
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    x = serializers.IntegerField()
    y = serializers.IntegerField()    

class TransformationSerializer(serializers.Serializer):

    resize = Resizeserializer(required=False)

    rotate = serializers.IntegerField(required=False)

    grayscale = serializers.BooleanField(required=False)

    sepia = serializers.BooleanField(required=False)

    format = serializers.ChoiceField(
        choices=["JPEG", "PNG", "WEBP"],
        required=False
    )    

    



        

