from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)
    extra = 1


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owners__full_name',)
    readonly_fields = ('created_at',)
    inlines = [OwnerInline]
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'get_owners',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)

    @admin.display(description='Собственники')
    def get_owners(self, obj):
        return ', '.join(owner.full_name for owner in obj.owners.all())


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('complainant', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('full_name', 'pure_phone')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
