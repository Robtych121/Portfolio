from django.shortcuts import render
from .models import Portfolios


# Create your views here.
def mainportfolio(request):
    portfolios = Portfolios.objects.filter(published='Yes').order_by('order')
    categories = Portfolios.objects.values_list('category', flat=True).distinct()

    return render(request, 'main_portfolio.html', {'portfolios': portfolios, 'categories': categories})
