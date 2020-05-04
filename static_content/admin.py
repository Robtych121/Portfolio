from django.contrib import admin
from .models import Static_Page

# Register your models here.
class StaticContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_date', 'updated_date')



admin.site.register(Static_Page, StaticContentAdmin)