# Generated by Django 4.2.2 on 2023-06-11 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_payments_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
