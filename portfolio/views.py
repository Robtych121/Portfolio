from django.shortcuts import render
from .models import main_portfolio

# Create your views here.

def main_portfolio(request):
    return render(request, 'main_portfolio.html')
