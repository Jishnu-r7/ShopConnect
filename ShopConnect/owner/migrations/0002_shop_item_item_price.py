# Generated by Django 4.2.2 on 2023-06-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_item',
            name='Item_Price',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
    ]
