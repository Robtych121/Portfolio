from django.urls import path
from .views import main_portfolio

urlpatterns = [
    path('', main_portfolio, name="main_portfolio")
]