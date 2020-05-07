from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Static_Page

# Create your views here.
def static_page(request, url):
    page = get_object_or_404(Static_Page, url=url)

    if(page.published == 'Yes'):
        return render(request, 'static_page.html', {'page': page})
    else:
        return render(request, 'not_active_static_page.html')