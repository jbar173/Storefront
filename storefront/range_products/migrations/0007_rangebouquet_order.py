# Generated by Django 3.1.2 on 2021-01-22 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210122_1804'),
        ('range_products', '0006_remove_rangebouquet_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='rangebouquet',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_bouquet', to='orders.order'),
        ),
    ]
