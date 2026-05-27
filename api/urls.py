from django.urls import path
from .views import UploadImageView

urlpatterns = [
    path("images/", UploadImageView.as_view())
]