from django.urls import path
from gallery.views import index

urlpatterns = [
    path('', index),
]