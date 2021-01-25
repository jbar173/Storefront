# Generated by Django 3.1.2 on 2021-01-15 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0008_basket_order'),
        ('orders', '0004_auto_20210115_1917'),
        ('themed_products', '0004_auto_20210115_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='RangeBouquet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('basket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='range_bouquet', to='basket.basket')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_bouquet', to='orders.order')),
            ],
        ),
    ]