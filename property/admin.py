from django.contrib import admin
from property.models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 
                    'construction_year', 'town',
                    'owners_phonenumber', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('likes',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ('flats',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('complainant', 'flat')


