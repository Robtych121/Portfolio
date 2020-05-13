from django.urls import path
from .views import contactForm

urlpatterns = [
    path('', contactForm, name="ContactForm")
]