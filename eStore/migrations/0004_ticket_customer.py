# Generated by Django 4.0 on 2022-01-13 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eStore', '0003_rename_customerdevice_customer_device_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eStore.customer'),
        ),
    ]
