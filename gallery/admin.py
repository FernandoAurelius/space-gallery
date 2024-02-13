from django.contrib import admin
from gallery.models import Photography

class ListPhotographs(admin.ModelAdmin):
    list_display = ('id', 'name', 'subtitle')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')

admin.site.register(Photography, ListPhotographs)