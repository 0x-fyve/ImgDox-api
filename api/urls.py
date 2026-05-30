from django.urls import path
from .views import UploadImageView, ListImagesView, RetrieveImagesView, ResizeImageView, RotateImageView
from .views import SepiaImageView, GrayscaleImageView, ConvertFormatView, CropImageView, TransformImageView

urlpatterns = [
    path("images/", UploadImageView.as_view()),
    path("images/list/", ListImagesView.as_view()),
    path("images/<int:pk>/", RetrieveImagesView.as_view()),
    path("images/<int:pk>/resize/", ResizeImageView.as_view()),
    path("images/<int:pk>/rotate/", RotateImageView.as_view()),
    path("images/<int:pk>/grayscale/", GrayscaleImageView.as_view()),
    path("images/<int:pk>/sepia/", SepiaImageView.as_view()),
    path("images/<int:pk>/format/", ConvertFormatView.as_view()),
    path("images/<int:pk>/crop/", CropImageView.as_view()),
    path("images/<int:pk>/transform/", TransformImageView.as_view()),
    
]