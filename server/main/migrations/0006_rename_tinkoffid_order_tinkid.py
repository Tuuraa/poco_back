# Generated by Django 5.0.3 on 2024-04-11 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_totalprice_order_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tinkoffID',
            new_name='tinkID',
        ),
    ]
