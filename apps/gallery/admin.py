from django.contrib import admin
from apps.gallery.models import Photography


class ListPhotographs(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle", "category", "published")
    list_display_links = ("name",)
    search_fields = ("name", "id")
    list_filter = (
        "category",
        "user",
    )
    list_per_page = 10
    list_editable = ("published",)


admin.site.register(Photography, ListPhotographs)
