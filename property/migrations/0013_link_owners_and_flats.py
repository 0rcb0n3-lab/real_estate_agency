from django.db import migrations


def link_owners_and_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.iterator():
        owner = Owner.objects.filter(
            owner=flat.owner,
            owner_phone_number=flat.owners_phonenumber,
        ).first()
        if owner:
            owner.flats.add(flat)


def unlink_owners_and_flats(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.iterator():
        owner.flats.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_fill_owners'),
    ]

    operations = [
        migrations.RunPython(link_owners_and_flats, unlink_owners_and_flats),
    ]
