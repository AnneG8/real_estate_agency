# Generated by Django 2.2.24 on 2023-07-27 18:25

from django.db import migrations


def fill_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        new_building = True if flat.construction_year >= 2015 else False
        Flat.objects.update_or_create(
            town=flat.town,
            address=flat.address,
            owner=flat.owner,
            defaults={'new_building': new_building
        })



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building),
    ]
