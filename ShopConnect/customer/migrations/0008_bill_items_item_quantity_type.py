# Generated by Django 4.2.2 on 2023-06-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_cart_item_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill_items',
            name='Item_Quantity_Type',
            field=models.CharField(default=12, max_length=7),
            preserve_default=False,
        ),
    ]
