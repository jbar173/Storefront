# Generated by Django 3.1.2 on 2021-01-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_basket_b_id_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
