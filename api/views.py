from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import  get_object_or_404

from .models import Image


from .serializers import Imageserializer
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

