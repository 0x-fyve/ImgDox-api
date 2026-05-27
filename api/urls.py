from django.urls import path
from .views import UploadImageView, ListImagesView

urlpatterns = [
    path("images/", UploadImageView.as_view()),
    path("images/list/", ListImagesView.as_view()),
]