import phonenumbers

from django.db import migrations


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.iterator():
        parsed = None
        try:
            parsed = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        except phonenumbers.NumberParseException:
            parsed = None
        if parsed and phonenumbers.is_valid_number(parsed):
            flat.owner_pure_phone = phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.E164,
            )
            flat.save(update_fields=['owner_pure_phone'])


def unfill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner_pure_phone=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone, unfill_owner_pure_phone),
    ]
