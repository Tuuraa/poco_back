# Generated by Django 5.0.3 on 2024-04-11 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_order_readies_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
