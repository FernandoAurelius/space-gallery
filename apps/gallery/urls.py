from django.urls import path
from apps.gallery.views import index, image, search, upload, edit, delete, filt, home

urlpatterns = [
    path("", home, name="home"),
    path("gallery", index, name="index"),
    path("image/<int:photo_id>", image, name="image"),
    path("search", search, name="search"),
    path("upload", upload, name="upload"),
    path("edit/<int:photo_id>", edit, name="edit"),
    path("delete/<int:photo_id>", delete, name="delete"),
    path("filt/<str:category>", filt, name="filt"),
]
