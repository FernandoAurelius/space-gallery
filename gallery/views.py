from django.shortcuts import render, get_object_or_404

from gallery.models import Photography

def index(request):
    photographys = Photography.objects.order_by('-release_date').filter(published=True)
    return render(request, 'gallery/index.html', {"cards": photographys})

def image(request, photo_id):
    photo = get_object_or_404(Photography, pk=photo_id)
    return render(request, 'gallery/image.html', {'photography': photo})