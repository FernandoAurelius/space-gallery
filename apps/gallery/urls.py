from django.urls import path
from apps.gallery.views import index, image, search, upload, edit, delete

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:photo_id>', image, name='image'),
    path('search', search, name='search'),
    path('upload', upload, name='upload'),
    path('edit', edit, name='edit'),
    path('delete', delete, name='delete')
]