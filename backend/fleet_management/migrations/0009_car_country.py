# Generated by Django 2.1.2 on 2019-07-24 17:23

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0008_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='country',
            field=django_countries.fields.CountryField(default='UA', max_length=2),
            preserve_default=False,
        ),
    ]
