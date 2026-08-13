from django.db import migrations


def fill_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner, phone, pure_phone in Flat.objects.values_list(
            'owner', 'owners_phonenumber', 'owner_pure_phone').iterator():
        Owner.objects.get_or_create(
            owner=owner,
            owner_phone_number=phone,
            defaults={'owner_pure_phone': pure_phone},
        )


def unfill_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_alter_owner_owner_phone_number'),
    ]

    operations = [
        migrations.RunPython(fill_owners, unfill_owners),
    ]
