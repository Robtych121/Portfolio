from django.contrib import admin
from .models import Portfolios


def publish_portfolio(modeladmin, request, queryset):
    queryset.update(published='Yes')
    publish_portfolio.short_description = "Publish Portfolio"
    publish_portfolio.allowed_permissions = ('change',)


def unpublish_portfolio(modeladmin, request, queryset):
    queryset.update(published='No')
    unpublish_portfolio.short_description = "Unpublish Portfolio"
    unpublish_portfolio.allowed_permissions = ('change',)

class PortfoliosAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'created_date', 'published')
    actions = [publish_portfolio,unpublish_portfolio]

# Register your models here.
admin.site.register(Portfolios, PortfoliosAdmin)