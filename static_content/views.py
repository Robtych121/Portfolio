from django.shortcuts import render
from .models import Static_Page

# Create your views here.
def static_page(request, url):
    pages = Static_Page.objects.filter(url=url)
    return render(request, 'static_page.html', {'pages': pages})