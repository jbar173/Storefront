# Generated by Django 3.1.2 on 2021-01-14 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210113_2056'),
        ('themed_products', '0002_themedbouquet_theme_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='themedbouquet',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='t_bouquet', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='themedbouquet',
            name='theme_name',
            field=models.CharField(choices=[('Type', 'Type'), ('Colour', 'Colour'), ('Type and Colour', 'Type and Colour')], max_length=50, null=True),
        ),
    ]