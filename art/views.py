from django.shortcuts import render
from .models import ArtProject

# Create your views here.
def index(request):
    context = {
        "arts": ArtProject.objects.order_by('-date')
    }

    return render(request, "art/index.html", context)

def about(request):
    return render(request, "art/about.html")

def gallery(request):
    return render(request, "art/gallery.html")