from django.urls import path
from .views import static_page

urlpatterns = [
    path('<str:url>/', static_page, name="static_page")
]