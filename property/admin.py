from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'flat_owners__owner',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'get_owners',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)

    @admin.display(description='Собственники')
    def get_owners(self, obj):
        return ', '.join(owner.owner for owner in obj.flat_owners.all())


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('owner', 'owner_pure_phone')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
