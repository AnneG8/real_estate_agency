from django.contrib import admin
from property.models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town, address, owner']
# admin.site.register(Flat, FlatAdmin)



