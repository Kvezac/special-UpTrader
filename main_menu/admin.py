from django.contrib import admin
from .models import Menu, Item


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_filter = ("menu",)
    fieldsets = (
        ("Add new item", {
            "description": "Parent should be a menu or item",
            "fields": (("menu", "parent"), "title", "slug")
        }),
    )
    # readonly_fields = ["slug"]
    prepopulated_fields = {"slug": ("title",)}
