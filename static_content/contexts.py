from django.shortcuts import get_object_or_404
from .models import Static_Page


def cart_menu_items(request):
    menu_items = Static_Page.objects.filter(onmenu='Yes').order_by('order')

    return { 'menu_items':menu_items }