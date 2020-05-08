from django.contrib import admin
from .models import Static_Page

def publish_page(modeladmin, request, queryset):
    queryset.update(published='Yes')
    publish_page.short_description = "Publish Page"
    publish_page.allowed_permissions = ('change',)


def unpublish_page(modeladmin, request, queryset):
    queryset.update(published='No')
    unpublish_page.short_description = "Unpublish Page"
    unpublish_page.allowed_permissions = ('change',)


def add_to_menu(modeladmin, request, queryset):
    queryset.update(onmenu='Yes')
    add_to_menu.short_description = "Add the page to the main menu"
    add_to_menu.allowed_permissions = ('change',)


def remove_from_menu(modeladmin, request, queryset):
    queryset.update(onmenu='No')
    remove_from_menu.short_description = "Remove the page from the main menu"
    remove_from_menu.allowed_permissions = ('change',)


class StaticContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'created_date', 'updated_date','published','onmenu')
    actions = [publish_page,unpublish_page,add_to_menu,remove_from_menu]


admin.site.register(Static_Page, StaticContentAdmin)