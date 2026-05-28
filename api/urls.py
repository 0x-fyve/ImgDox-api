from django.urls import path
from .views import UploadImageView, ListImagesView, RetrieveImagesView

urlpatterns = [
    path("images/", UploadImageView.as_view()),
    path("images/list/", ListImagesView.as_view()),
    path("images/<int:pk>/", RetrieveImagesView.as_view()),
]