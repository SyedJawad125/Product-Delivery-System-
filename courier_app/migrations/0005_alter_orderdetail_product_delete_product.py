# Generated by Django 5.0.3 on 2024-05-02 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier_app', '0004_alter_order_status'),
        ('permission_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail_product', to='permission_app.product'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
