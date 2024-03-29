# Generated by Django 3.1.2 on 2020-12-05 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201205_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('billing_address', models.TextField(blank=True)),
                ('delivery_address', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_account', to='accounts.user')),
            ],
        ),
    ]
