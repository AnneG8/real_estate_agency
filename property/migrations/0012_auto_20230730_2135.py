# Generated by Django 2.2.24 on 2023-07-30 18:35

from django.db import migrations


def fill_owner_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(
            name=flat.owner,
            pure_phone=flat.owner_pure_phone,
            defaults = {'phonenumber': flat.owners_phonenumber}
        )[0]
        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owner_model),
    ]
