# Generated by Django 5.0.3 on 2024-05-03 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier_app', '0006_remove_orderdetail_product_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_by',
            new_name='added_by',
        ),
    ]