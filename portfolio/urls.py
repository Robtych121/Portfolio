from django.urls import path
from .views import mainportfolio, view_portfolio

urlpatterns = [
    path('', mainportfolio, name="mainportfolio"),
    path('view/<int:id>/', view_portfolio, name="view_portfolio")
]