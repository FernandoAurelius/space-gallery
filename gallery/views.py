from django.shortcuts import render, get_object_or_404

from gallery.models import Photography

def index(request):
    photographys = Photography.objects.order_by('-release_date').filter(published=True)
    return render(request, 'gallery/index.html', {"cards": photographys})

def image(request, photo_id):
    photo = get_object_or_404(Photography, pk=photo_id)
    return render(request, 'gallery/image.html', {'photography': photo})

def search(request):
    photographys = Photography.objects.order_by('-release_date').filter(published=True)

    if "search" in request.GET:
        name_search = request.GET['search']
        if name_search:
            photographys = photographys.filter(name__icontains=name_search)

    return render(request, 'gallery/search.html', {'cards': photographys})