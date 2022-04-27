# Generated by Django 4.0.3 on 2022-04-27 21:46

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_remove_manager_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='', max_length=63),
        ),
        migrations.AlterField(
            model_name='merchandiser',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
