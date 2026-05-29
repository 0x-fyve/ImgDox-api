from django.urls import path
from .views import UploadImageView, ListImagesView, RetrieveImagesView, ResizeImageView, RotateImageView, GrayscaleImageView

urlpatterns = [
    path("images/", UploadImageView.as_view()),
    path("images/list/", ListImagesView.as_view()),
    path("images/<int:pk>/", RetrieveImagesView.as_view()),
    path("images/<int:pk>/resize/", ResizeImageView.as_view()),
    path("images/<int:pk>/rotate/", RotateImageView.as_view()),
    path("images/<int:pk>/rotate/", GrayscaleImageView.as_view()),
]