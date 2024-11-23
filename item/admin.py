from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type', 'item_status', 'color', 'available')
    list_filter = ('type', 'item_status', 'available')
    search_fields = ('name', 'slug', 'color')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

# admin.site.register(Item, ItemAdmin)
