# Generated by Django 3.1.2 on 2021-01-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('range_products', '0002_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='rangebouquet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]