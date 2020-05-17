from django.shortcuts import render
from .models import Portfolios


# Create your views here.
def mainportfolio(request):
    portfolios = Portfolios.objects.filter(published='Yes').order_by('order')
    categories = Portfolios.objects.values_list('category', flat=True).distinct()

    return render(request, 'main_portfolio.html', {'portfolios': portfolios, 'categories': categories})


def view_portfolio(request, id):
    portfolio = Portfolios.objects.get(id=id)

    return render(request, 'view_portfolio.html', {'portfolio': portfolio})