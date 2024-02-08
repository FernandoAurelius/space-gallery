from django.shortcuts import render

def index(request):
    return render(request, 'gallery/index.html')

def image(request):
    return render(request, 'gallery/image.html')