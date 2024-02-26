from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from apps.gallery.models import Photography
from apps.gallery.forms import PhotographyForm

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria!')
        return redirect('login')

    photographys = Photography.objects.order_by('-release_date').filter(published=True)
    return render(request, 'gallery/index.html', {"cards": photographys})

def image(request, photo_id):
    photo = get_object_or_404(Photography, pk=photo_id)
    return render(request, 'gallery/image.html', {'photography': photo})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria!')
        return redirect('login')

    photographys = Photography.objects.order_by('-release_date').filter(published=True)

    if "search" in request.GET:
        name_search = request.GET['search']
        if name_search:
            photographys = photographys.filter(name__icontains=name_search)

    return render(request, 'gallery/search.html', {'cards': photographys})

def upload(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria!')
        return redirect('login')
    
    form = PhotographyForm()
    if request.method == 'POST':
        form = PhotographyForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Fotografia foi salva com sucesso!')
            return redirect(index)

    return render(request, 'gallery/upload.html', {'form': form})

def edit(request, photo_id):
    photo = Photography.objects.get(id=photo_id)
    form = PhotographyForm(instance=photo)

    if request.method == 'POST':
        form = PhotographyForm(request.POST, request.FILES, instance=photo)
        if form.is_valid:
            form.save()
            messages.success(request, 'Fotografia foi salva com sucesso!')
            return redirect(index)

    return render(request, 'gallery/edit.html', {'form': form, 'photo_id': photo_id})

def delete(request, photo_id):
    photo = Photography.objects.get(id=photo_id)
    photo.delete()
    messages.success(request, 'Fotografia foi deletada com sucesso!')
    return redirect(index)

def filt(request, category):
    photographys = Photography.objects.order_by('-release_date').filter(published=True, category=category)
    
    return render(request, 'gallery/index.html', {"cards": photographys})
