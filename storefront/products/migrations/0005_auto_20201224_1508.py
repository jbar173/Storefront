# Generated by Django 3.1.2 on 2020-12-24 15:08

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_bouquet_fave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bouquet',
            name='fave',
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8),
        ),
    ]
