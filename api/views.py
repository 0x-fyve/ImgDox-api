from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import  get_object_or_404
import os

from .models import Image
from .serializers import Imageserializer, Resizeserializer, Rotateserializer, FormatSerializer, CropSerializer, TransformationSerializer
from .services import resize_image, rotate_image, grayscale_image, sepia_image, convert_image_format,crop_image, apply_transformations
# Create your views here.

class UploadImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = Imageserializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(serializer.data,
            status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    
class ListImagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        images = Image.objects.filter(user=request.user)

        serializer = Imageserializer(images, many=True)

        return Response(serializer.data)
    
class RetrieveImagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        image = get_object_or_404(Image, id=pk, user=request.user)

        serializer = Imageserializer(image)

        return Response(serializer.data)
    
class ResizeImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        image = get_object_or_404(Image, id=pk, user=request.user)

        serializer = Resizeserializer(data=request.data)

        if serializer.is_valid():
            width = serializer.validated_data["width"]
            height = serializer.validated_data["height"]

            new_filename = resize_image(image.image.path, width, height)

            image_url = request.build_absolute_uri(
                f"/media/uploads/{new_filename}"
            )           
            return Response({
                "resized_image": image_url
            })

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

            
class RotateImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        image = get_object_or_404(
            Image,
            id=pk,
            user=request.user
        )

        serializer = Rotateserializer(data=request.data)

        if serializer.is_valid():

            angle = serializer.validated_data["angle"]

            new_path = rotate_image(image.image.path, angle)


            return Response({
                    "original": request.build_absolute_uri(image.image.url),
                    "transformed": request.build_absolute_uri(
                        "/media/" + new_path.split("media/")[-1]
                    )
            })

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class GrayscaleImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        image = get_object_or_404(
            Image,
            id=pk,
            user=request.user
        )

        new_filename = grayscale_image(image.image.path)

        image_url = request.build_absolute_uri(
            f"/media/uploads/{new_filename}"
        )

        return Response({
            "grayscale_image": image_url
        })
    
class SepiaImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        image = get_object_or_404(
            Image,
            id=pk,
            user=request.user
        )

        new_filename = sepia_image(image.image.path)

        image_url = request.build_absolute_uri(
            f"/media/uploads/{new_filename}"
        )

        return Response({
            "sepia_img": image_url
        })

class ConvertFormatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        image = get_object_or_404(
            Image,
            id=pk,
            user=request.user
        )

        serializer = FormatSerializer(data=request.data)

        if serializer.is_valid():

            new_format = serializer.validated_data["format"]

            new_filename = convert_image_format(
                image.image.path,
                new_format
            )

            image_url = request.build_absolute_uri(
                f"/media/uploads/{new_filename}"
            )

            return Response({
                "converted_image": image_url
            })

        return Response(serializer.errors,
                        status=400)
    
class CropImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        image = get_object_or_404(
            Image,
            id=pk,
            user=request.user
        )

        serializer = CropSerializer(data=request.data)

        if serializer.is_valid():

            data = serializer.validated_data

            new_filename = crop_image(
                image.image.path,
                data["width"],
                data["height"],
                data["x"],
                data["y"]
            )

            image_url = request.build_absolute_uri(
                f"/media/uploads/{new_filename}"
            )

            return Response({
                "cropped_image": image_url
            })

        return Response(serializer.errors,
                        status=400)


class TransformImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        image = get_object_or_404(
            Image,
            id=pk,
            user=request.user
        )

        serializer = TransformationSerializer(
            data=request.data.get("transformations", {})
        )

        if serializer.is_valid():

            transformed_path = apply_transformations(
                image.image.path,
                serializer.validated_data
            )

            filename = os.path.basename(transformed_path)

            image_url = request.build_absolute_uri(
                f"/media/uploads/{filename}"
            )

            return Response({
                "transformed_image": image_url
            })

        return Response(serializer.errors, status=400)