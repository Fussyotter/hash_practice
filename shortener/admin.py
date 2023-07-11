from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url', 'pub_date', 'count')
    list_filter = ('pub_date',)
    search_fields = ('long_url', 'short_url')
    readonly_fields = ('short_url', 'pub_date', 'count')

    
    