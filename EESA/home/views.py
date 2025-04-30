from django.shortcuts import render
from .models import *
import os, base64
from django.conf import settings

def home(request):
    logo = LogoImages.objects.get(title='eesa-logo')
    council = CouncilPhotos.objects.all()

    slides = SlideImage.objects.all()
    return render(request, 'home.html', {'slides': slides, "logo": logo, "council": council})

def contents(request):
    logo = LogoImages.objects.get(title='eesa-logo')

    blogs = Blog.objects.all()
    return render(request, 'imp-links.html', {'blogs': blogs, 'logo': logo})
