from django.urls import path
from .views import mainportfolio

urlpatterns = [
    path('', mainportfolio, name="mainportfolio")
]