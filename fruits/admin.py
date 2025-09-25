from django.contrib import admin

from .models import Fruit
class FruitAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Fruit, FruitAdmin)
